from project.models import Organization, Project


def global_vars(request):
    ctx = {}
    ctx['top_ongs'] = Organization.top()
    ctx['top_projects'] = Project.top()
    return ctx
