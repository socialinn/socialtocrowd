from django.views.generic.base import TemplateView
from project.models import Project
from project.models import Thing
from project.models import Donation


class Index(TemplateView):
    template_name = 'landing/index.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super(Index, self).get_context_data(*args, **kwargs)
        ctx['top_projects'] = Project.top(3)
        ctx["all_projects"] = Project.latests(5)

        # Latests project bigger need
        needs = []
        for p in Project.latests(4):
            need = p.things.all().order_by("quantity")
            if not need:
                continue
            needs.append(need[0])

        ctx["needs"] = needs
        ctx["donnors"] = Donation.objects.all().order_by('-shipping__created')
        return ctx


index = Index.as_view()
