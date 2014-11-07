from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

from django.views.generic.base import TemplateView
from project.models import Shipping


class Profile(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super(Profile, self).get_context_data(*args, **kwargs)
        shippings = Shipping.objects.filter(user=self.request.user.id)
        ctx['shippings'] = shippings
        return ctx

profile = login_required(Profile.as_view())
