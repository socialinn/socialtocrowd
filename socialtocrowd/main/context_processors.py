from project.models import Organization


def global_vars(request):
    ctx = {}
    ctx['top_ongs'] = Organization.top()
    return ctx
