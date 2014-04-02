from django.views.generic.base import TemplateView
from django.utils.translation import ugettext as _


class Near(TemplateView):
    template_name = 'project/near.html'
near = Near.as_view()


class Things(TemplateView):
    template_name = 'project/search.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super(Things, self).get_context_data(*args, **kwargs)
        ctx['title'] = _('Donate')
        ctx['placeholder'] = _('Search things to donate')
        return ctx
things = Things.as_view()


class ONGs(TemplateView):
    template_name = 'project/search.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super(ONGs, self).get_context_data(*args, **kwargs)
        ctx['title'] = _('ONGs')
        ctx['placeholder'] = _('Search ONG to donate')
        return ctx
ongs = ONGs.as_view()
