from django.views.generic.base import TemplateView


class Near(TemplateView):
    template_name = 'project/near.html'
near = Near.as_view()
