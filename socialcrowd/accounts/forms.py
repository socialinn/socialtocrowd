from django import forms
from django.utils.translation import ugettext as _
from accounts.models import MyUser


class RegisterForm(forms.Form):
    email = forms.EmailField(max_length=100,
                             required=True,
                             widget=forms.TextInput(attrs={'placeholder': _('Email'),
                                                           'required': 'required'}))
    password = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': _('Password'),
                                                                 'required': 'required'}))
    password2 = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': _('Repeat the password'),
                                                                  'required': 'required',
                                                                  'data-error': _("The password didn't match")}))

    def save(self):
        email = self.cleaned_data['email']
        paswd = self.cleaned_data['password']
        u = MyUser(email=email)
        u.set_password(paswd)
        u.save()
        return u
