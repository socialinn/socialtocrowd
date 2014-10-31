from django.db import models
from django.contrib.auth.models import User


class Organization(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    img = models.ImageField(upload_to="ongs", blank=True, null=True)
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    img = models.ImageField(upload_to="projects", blank=True, null=True)
    ong = models.ForeignKey(Organization, related_name='projects')
    shipping_address = models.TextField()
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


class Donation(models.Model):
    STATUS = (
        ('sent', 'sent'),
        ('received', 'received'),
        ('confirmed', 'confirmed'),
    )
    thing = models.ForeignKey(Thing, related_name='donations')
    donor = models.ForeignKey(User, related_name='donations')
    info = models.TextField(blank=True)
    status = models.CharField(choices=STATUS, max_length=10, default="sent")
    quantity = models.IntegerField(default=1)

    created = models.DateTimeField(auto_now_add=True)

    def project(self):
        return self.thing.project

    def __unicode__(self):
        return self.thing.name
