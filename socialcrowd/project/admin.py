from django.contrib import admin
from project import models


admin.site.register(models.Organization)
admin.site.register(models.Donation)
admin.site.register(models.Project)
admin.site.register(models.Thing)
admin.site.register(models.Shipping)
admin.site.register(models.ShippingCompany)
