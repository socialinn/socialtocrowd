from django.db.models import Q
from django.views.generic.base import TemplateView
from django.utils.translation import ugettext as _

from .models import Project
from .models import Organization


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
