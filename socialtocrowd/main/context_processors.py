from project.models import Organization


def global_vars(request):
    ctx = {}
    ctx['top_ongs'] = Organization.objects.all()[0:5]
    return ctx
