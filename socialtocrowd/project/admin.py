from django.contrib import admin
from project import models
from django.utils.translation import ugettext as _


def make_active(modeladmin, request, queryset):
    queryset.update(status='active')
make_active.short_description = _("Mark selected ongs as active")

class OrgAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'status', 'city')
    list_filter = ('status', )
    actions = [make_active, ]

class ProjectObjectiveInline(admin.TabularInline):
    model = models.ProjectObjective

class ProjectAdmin(admin.ModelAdmin):
    model = models.Project
    inlines = [ ProjectObjectiveInline ]

admin.site.register(models.Organization, OrgAdmin)

admin.site.register(models.Donation)
admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.ProjectObjective)
admin.site.register(models.Thing)
admin.site.register(models.Direction)
admin.site.register(models.Cooperation)
admin.site.register(models.Shipping)
admin.site.register(models.ShippingCompany)
admin.site.register(models.Category)
admin.site.register(models.Collaborator)
