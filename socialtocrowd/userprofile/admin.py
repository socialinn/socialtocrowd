from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from . import models


class UserProfileInline(admin.StackedInline):
    model = models.Profile

    def has_delete_permission(self, request, obj=None):
        return False


class MyUserAdmin(UserAdmin):
    inlines = [
        UserProfileInline,
    ]

admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)

admin.site.register(models.Profile)
