from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.views.generic.base import TemplateView
from project.models import Shipping

from .forms import EditProfileForm


class Profile(TemplateView):
    template_name = 'userprofile/profile.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super(Profile, self).get_context_data(*args, **kwargs)
        shippings = Shipping.objects.filter(user=self.request.user.id)
        ctx['shippings'] = shippings
        return ctx
profile = login_required(Profile.as_view())


class EditProfile(TemplateView):
    template_name = 'userprofile/edit.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super(EditProfile, self).get_context_data(*args, **kwargs)
        ctx['form'] = EditProfileForm(instance=self.request.user.profile)
        return ctx

    def post(self, request):
        f = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if f.is_valid():
            f.save()

            return redirect('profile')
        else:
            ctx = self.get_context_data()
            ctx['form'] = f
            return render(request, self.template_name, ctx)

editProfile = login_required(EditProfile.as_view())
