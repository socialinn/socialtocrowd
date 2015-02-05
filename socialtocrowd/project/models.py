from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.contrib.gis.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save, post_save

class Organization(models.Model):
    STATUS = (
        ('pending', 'pending'),
        ('active', 'active'),
        ('deleted', 'deleted'),
    )

    user = models.ForeignKey(User, related_name='organizations')
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, null=True, max_length=150)
    description = models.TextField(blank=True)
    img = models.ImageField(upload_to="ongs", blank=True, null=True)
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    status = models.CharField(choices=STATUS, max_length=10, default="pending")

    def fillslug(self):
        self.slug = slugify(self.name)
        post_save.disconnect(post_add_ong, sender=Organization)
        self.save()
        post_save.connect(post_add_ong, sender=Organization)
        return self.slug

    def getslug(self):
        return self.slug or self.fillslug()

    @classmethod
    def top(cls, n=5):
        return cls.objects.all().order_by("-pk")[0:n]

    def __unicode__(self):
        return self.name

def post_add_ong(sender, instance, created, *args, **kwargs ):
    instance.fillslug()

post_save.connect(post_add_ong, sender=Organization)



class Project(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, null=True, max_length=150)
    description = models.TextField()
    img = models.ImageField(upload_to="projects", blank=True, null=True)
    ong = models.ForeignKey(Organization, related_name='projects')
    hashtag = models.CharField(max_length=255, blank=True, null=True)
    objetives = models.CharField(max_length=255)
    images = models.CharField(max_length=255, blank=True, null=True)
    video = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    twitter = models.CharField(max_length=150, default="https://twitter.com/")
    googleplus = models.CharField(max_length=255, default="https://plus.google.com/", verbose_name="Google+")
    facebook = models.CharField(max_length=255, default="https://www.facebook.com/")
    website = models.URLField(blank=True, null=True)

    def fillslug(self):
        self.slug = slugify(self.name)
        post_save.disconnect(post_add_project, sender=Project)
        self.save()
        post_save.connect(post_add_project, sender=Project)
        return self.slug

    def getslug(self):
        return self.slug or self.fillslug()

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.slug)])

    @classmethod
    def top(cls, n=5):
        return cls.objects.all().order_by("-pk")[0:n]

    @classmethod
    def latests(cls, n=5):
        return cls.objects.all().order_by("-created")[0:n]

    def __unicode__(self):
        return self.name

    def remain_things(self):
        total = 0
        for thing in self.things.all():
            total += thing.quantity
            total -= thing.ndonations().get('total')
        if total < 0:
            total = 0
        return total

    def percent_donate(self):
        total_things_needed = 0
        total_things_donated = 0
        percentage_donated = 0
        for thing in self.things.all():
            total_things_needed += thing.quantity
            thing_donations = min(thing.quantity, thing.ndonations().get('total'))
            total_things_donated += thing_donations
        if total_things_donated <= 0:
            percentage_donated = 0
        else:
            percentage_donated = total_things_donated * 100.0 / total_things_needed
        print(total_things_needed)
        print(total_things_donated)
        return min(percentage_donated, 100)

    def get_objetives(self):
        if self.objetives is None:
            return ''
        return self.objetives.split(',')

    def get_images(self):
        if self.images is None:
            return ''
        return self.images.split(',')

def post_add_project(sender, instance, created, *args, **kwargs ):
    instance.fillslug()

post_save.connect(post_add_project, sender=Project)

class ProjectObjective(models.Model):
    project = models.ForeignKey(Project, related_name='objectives')
    manifest = models.CharField(max_length=255)


class Thing(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    project = models.ForeignKey(Project, related_name='things')
    quantity = models.IntegerField(default=1)

    def ndonations(self):
        total = 0
        sent = 0
        received = 0
        creating = 0
        for donation in self.donations.all():
            if donation.shipping.status == 'sent':
                sent += donation.quantity
            elif donation.shipping.status == 'received':
                received += donation.quantity
            elif donation.shipping.status == 'creating':
                creating += donation.quantity
                total -= donation.quantity
            total += donation.quantity
        return {'received': received, 'sent': sent, 'creating': creating,
                'total': total, 'nodonate': self.quantity - total }

    def __unicode__(self):
        return self.name

    def serialize(self):
        d = {
            'name': self.name,
        }
        return d


class Direction(models.Model):
    project = models.ForeignKey(Project, related_name='directions')
    description = models.CharField(max_length=255)
    pos = models.PointField(blank=True, null=True)
    timetable = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __unicode__(self):
        timetable = ""
        phone = ""
        if self.timetable:
            timetable = "Available time: " + self.timetable + ". "
        if self.phone:
            phone = "Tel: " + self.phone + ". "
        return self.description + timetable + phone


class Cooperation(models.Model):
    name = models.CharField(max_length=255)
    what = models.TextField()
    where = models.ForeignKey(Direction, related_name='cooperations', blank=True, null=True)
    when = models.DateTimeField(blank=True, null=True)
    project = models.ForeignKey(Project, related_name='cooperations')
    quantity = models.IntegerField(default=1)

    def remain(self):
        return self.quantity - self.cooperations.all().count()

    def __unicode__(self):
        return self.name

    def serialize(self):
        d = {
            'name': self.name,
        }
        return d


class Shipping(models.Model):
    STATUS = (
        ('sent', 'sent'),
        ('received', 'received'),
        ('confirmed', 'confirmed'),
        ('creating', 'creating'),
    )
    project = models.ForeignKey(Project, related_name='shipping')
    user = models.ForeignKey(User, related_name='shipping')
    comment = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    direction = models.ForeignKey(Direction, null=True, related_name='shipping')
    status = models.CharField(choices=STATUS, max_length=10, default="creating")
    delivery = models.DateTimeField(null=True)

    def __unicode__(self):
        return str(self.id)

    def serialize(self):
        d = {
            'id': self.id,
            'donations': [i.serialize() for i in self.donations.all()],
            'created': self.created.isoformat(),
        }
        return d


DONATION_TYPE = (
        ('C', 'Cooperation'),
        ('T', 'Thing'),
    )

class Donation(models.Model):
    thing = models.ForeignKey(Thing, related_name='donations', blank=True, null=True)
    cooperation = models.ForeignKey(Cooperation, related_name='cooperations', blank=True, null=True)
    type_donation = models.CharField(max_length=1, choices=DONATION_TYPE, default='T')
    shipping = models.ForeignKey(Shipping, related_name='donations')
    info = models.TextField(blank=True)
    quantity = models.IntegerField(default=1)
    img = models.ImageField(upload_to="donations", blank=True, null=True)
    show = models.BooleanField(default=True)

    def project(self):
        return self.shipping.project

    def donor(self):
        return self.shipping.user

    def created(self):
        return self.shipping.created

    def status(self):
        return self.shipping.status

    def __unicode__(self):
        return self.thing.name

    def serialize(self):
        d = {
            'id': self.id,
            'quantity': self.quantity,
        }
        if self.thing:
            d['thing'] = self.thing.serialize()
        elif self.cooperation:
            d['cooperation'] = self.cooperation.serialize()
        return d


class ShippingCompany(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    info = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    project = models.ForeignKey(Project, related_name='categories')
    name = models.CharField(max_length=25)

    def __unicode__(self):
        return self.name


class Collaborator(models.Model):
    project = models.ForeignKey(Project, related_name='collaborators')
    img = models.ImageField(upload_to="collaborators")
    link = models.CharField(max_length=255)

    def __unicode__(self):
        return self.link
