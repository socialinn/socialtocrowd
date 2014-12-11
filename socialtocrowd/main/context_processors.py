from project.models import Organization, Project


def global_vars(request):
    ctx = {}
    ctx['top_ongs'] = Organization.top()
    return ctx
