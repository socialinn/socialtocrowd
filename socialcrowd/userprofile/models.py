import os
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    avatar = models.ImageField(_("Avatar"), blank=True, null=True,
                               upload_to="photos")
    web = models.URLField(_("Web"), blank=True, null=True, default="")
    twitter = models.CharField("Twitter", max_length=100, blank=True, null=True, default="")
    facebook = models.CharField("Facebook", max_length=100, blank=True, null=True, default="")

    def __unicode__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    p, _ = Profile.objects.get_or_create(user=instance)
    p.save()
