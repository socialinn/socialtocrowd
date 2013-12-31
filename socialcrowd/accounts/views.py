from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import ugettext as _

from accounts.forms import RegisterForm


def logout_view(request):
    logout(request)
    return redirect('landing_index')


class Profile(TemplateView):
    template_name = 'accounts/profile.html'


class Register(TemplateView):
    template_name = 'accounts/register.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Register, self).get_context_data(*args, **kwargs)
        context['form'] = RegisterForm()
        return context

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            u = form.save()
            messages.success(request, _('Welcome %s, now you can login!') % u.email)
            return redirect('login')

        context = {}
        context['form'] = form
        return render(request, self.template_name, context)


profile = login_required(Profile.as_view())
register = Register.as_view()
