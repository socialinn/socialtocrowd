from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

from django.views.generic.base import TemplateView


class Profile(TemplateView):
    template_name = 'profile.html'


profile = login_required(Profile.as_view())
