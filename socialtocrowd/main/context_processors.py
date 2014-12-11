from project.models import Organization
from newsfeed.models import NewsCached


def global_vars(request):
    ctx = {}
    ctx['top_ongs'] = Organization.top()
    ctx['news'] = NewsCached.objects.all()[0:3]
    return ctx
