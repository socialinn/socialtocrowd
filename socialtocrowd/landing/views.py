from django.views.generic.base import TemplateView
from project.models import Project


class Index(TemplateView):
    template_name = 'landing/index.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super(Index, self).get_context_data(*args, **kwargs)
        ctx['top_projects'] = Project.top(3)
        ctx["all_projects"] = Project.latests(7)
        return ctx


index = Index.as_view()
