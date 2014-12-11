from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models


class Organization(models.Model):
    STATUS = (
        ('pending', 'pending'),
        ('active', 'active'),
        ('deleted', 'deleted'),
    )

    user = models.ForeignKey(User, related_name='organizations')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    img = models.ImageField(upload_to="ongs", blank=True, null=True)
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    status = models.CharField(choices=STATUS, max_length=10, default="pending")

    @classmethod
    def top(cls, n=5):
        return cls.objects.all().order_by("-pk")[0:n]

    def __unicode__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    img = models.ImageField(upload_to="projects", blank=True, null=True)
    ong = models.ForeignKey(Organization, related_name='projects')
    hashtag = models.CharField(max_length=255, blank=True, null=True)
    objetives = models.CharField(max_length=255)
    images = models.CharField(max_length=255, blank=True, null=True)
    video = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    @classmethod
    def top(cls, n=5):
        return cls.objects.all().order_by("-pk")[0:n]

    @classmethod
    def latests(cls, n=5):
        return cls.objects.all().order_by("-created")[0:n]

    def __unicode__(self):
        return self.name

    def percent_donate(self):
        total = 0
        donate = 0
        for thing in self.things.all():
            total += thing.quantity
            donate += thing.ndonations().get('total')
        if total <= 0:
            res = 0
        else:
            res = donate * 100.0 / total
        return res

    def get_objetives(self):
        return self.objetives.split(',')

    def get_images(self):
        return self.images.split(',')


class Thing(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    project = models.ForeignKey(Project, related_name='things')
    quantity = models.IntegerField(default=1)

    def ndonations(self):
        total = 0
        sent = 0
        received = 0
        for donation in self.donations.all():
            if donation.status == 'sent':
                sent += donation.quantity
            elif donation.status == 'received':
                sent += donation.quantity
            total += donation.quantity
        return {'received': received, 'sent': sent, 'total': total,
                'nodonate': self.quantity - total }

    def __unicode__(self):
        return self.name


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


class Shipping(models.Model):
    STATUS = (
        ('sent', 'sent'),
        ('received', 'received'),
        ('confirmed', 'confirmed'),
    )
    project = models.ForeignKey(Project, related_name='shipping')
    user = models.ForeignKey(User, related_name='shipping')
    comment = models.TextField(blank=True)
    show = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    direction = models.ForeignKey(Direction, null=True, related_name='shipping')
    status = models.CharField(choices=STATUS, max_length=10, default="sent")
    delivery = models.DateTimeField(null=True)

    def __unicode__(self):
        return str(self.id)


class Donation(models.Model):
    thing = models.ForeignKey(Thing, related_name='donations')
    shipping = models.ForeignKey(Shipping, related_name='donations')
    info = models.TextField(blank=True)
    quantity = models.IntegerField(default=1)

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
