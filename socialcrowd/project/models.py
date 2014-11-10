from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models


class Organization(models.Model):
    STATUS = (
        ('pending', 'pending'),
        ('actived', 'actived'),
        ('deleted', 'deleted'),
    )

    user = models.ForeignKey(User, related_name='organizations')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    img = models.ImageField(upload_to="ongs", blank=True, null=True)
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    status = models.CharField(choices=STATUS, max_length=10, default="pending")

    def __unicode__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    img = models.ImageField(upload_to="projects", blank=True, null=True)
    ong = models.ForeignKey(Organization, related_name='projects')
    created = models.DateTimeField(auto_now_add=True)

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
    #pos = models.GeoManager()
    pos = models.PointField(blank=True, null=True, help_text="Represented as (longitude, latitude)")

    timetable = models.CharField(max_length=255)
    phone = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.description


class Shipping(models.Model):
    project = models.ForeignKey(Project, related_name='shipping')
    user = models.ForeignKey(User, related_name='shipping')
    comment = models.TextField(blank=True)
    show = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def status(self):
        total = 0
        sent = 0
        received = 0
        for donation in self.donations.all():
            if donation.status == 'sent':
                sent += donation.quantity
            elif donation.status == 'received':
                sent += donation.quantity
            total += donation.quantity
        if total == received:
            return 'received'
        elif total == sent:
            return 'pending'
        else:
            return 'incomplete'

    def __unicode__(self):
        return str(self.id)


class Donation(models.Model):
    STATUS = (
        ('sent', 'sent'),
        ('received', 'received'),
        ('confirmed', 'confirmed'),
    )
    SENDTYPE = (
        ('donorpay', 'donor pay'),
        ('ongpay', 'ong pay'),
        ('free', 'free'),
    )
    thing = models.ForeignKey(Thing, related_name='donations')
    shipping = models.ForeignKey(Shipping, related_name='donations')
    direction = models.ForeignKey(Direction, related_name='donations')
    info = models.TextField(blank=True)
    status = models.CharField(choices=STATUS, max_length=10, default="sent")
    sendtype = models.CharField(choices=SENDTYPE, max_length=10, default="free")
    quantity = models.IntegerField(default=1)
    delivery = models.DateTimeField(null=True)

    def project(self):
        return self.shipping.project

    def donor(self):
        return self.shipping.user

    def created(self):
        return self.shipping.created

    def __unicode__(self):
        return self.thing.name


class ShippingCompany(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    info = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name
