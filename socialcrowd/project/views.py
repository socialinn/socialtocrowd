from django.db import models
from django.db.models import Q
from django.views.generic.base import TemplateView
from django.utils.translation import ugettext as _
from django.shortcuts import get_object_or_404, render

from .models import Project
from .models import Organization
from .models import Thing, Shipping, Donation


class Near(TemplateView):
    template_name = 'project/near.html'
near = Near.as_view()


class Things(TemplateView):
    template_name = 'project/search.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super(Things, self).get_context_data(*args, **kwargs)
        ctx['title'] = _('Donate')
        ctx['placeholder'] = _('Search things to donate')

        q = self.request.GET.get('search', '')
        # default
        query = Project.objects.all()
        complexq = Q()
        if q:
            complexq = complexq & Q(name__icontains=q)
            complexq = complexq | Q(description__icontains=q)
            complexq = complexq | Q(ong__name__icontains=q)
            complexq = complexq | Q(ong__description__icontains=q)
            complexq = complexq | Q(shipping_address__icontains=q)
            complexq = complexq | Q(things__name__icontains=q)
            complexq = complexq | Q(things__description__icontains=q)

        query = query.filter(complexq).distinct()

        # TODO paginate
        ctx['projects'] = query
        ctx['listtemplate'] = 'project/projects.html'
        return ctx
things = Things.as_view()


class ONGs(TemplateView):
    template_name = 'project/search.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super(ONGs, self).get_context_data(*args, **kwargs)
        ctx['title'] = _('ONGs')
        ctx['placeholder'] = _('Search ONG to donate')

        q = self.request.GET.get('search', '')
        # default
        query = Organization.objects.all()
        complexq = Q()
        if q:
            complexq = complexq & Q(name__icontains=q)
            complexq = complexq | Q(description__icontains=q)
            complexq = complexq | Q(projects__name__icontains=q)
            complexq = complexq | Q(projects__description__icontains=q)
            complexq = complexq | Q(city__icontains=q)
            complexq = complexq | Q(province__icontains=q)

        query = query.filter(complexq).distinct()

        # TODO paginate
        ctx['ongs'] = query
        ctx['listtemplate'] = 'project/ongs.html'
        return ctx
ongs = ONGs.as_view()


class Detail(TemplateView):
    template_name = 'project/project-detail.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super(Detail, self).get_context_data(*args, **kwargs)
        project = get_object_or_404(Project, pk=self.args[0])
        ctx['project'] = project
        return ctx
detail = Detail.as_view()


def donate(request, pk):
    project = get_object_or_404(Project, pk=pk)
    checks = []
    for c in request.GET.getlist('checks[]'):
        checks.append(int(c))
    ship_project = Shipping(project=project, user=request.user)
    ship_project.save()
    ctx = {}
    ctx['project'] = project
    ctx['things_checks'] = checks
    ctx['ship'] = ship_project
    ctx['sendtypes'] = Donation.SENDTYPE
    return render(request, 'project/donate-t1.html', ctx)
