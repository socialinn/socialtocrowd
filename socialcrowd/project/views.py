from django.db import models
from django.db.models import Q
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.utils.translation import ugettext as _
from django.shortcuts import get_object_or_404, render, redirect
from datetime import datetime

from .forms import ThingFormSet
from .models import Project
from .models import Organization
from .models import Thing, Shipping, Donation
from .models import ShippingCompany


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


class CreateONG(CreateView):
    model = Organization
    fields = ['name', 'description', 'img', 'city', 'province']
    success_url = '/'


class Detail(TemplateView):
    template_name = 'project/project-detail.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super(Detail, self).get_context_data(*args, **kwargs)
        project = get_object_or_404(Project, pk=self.args[0])
        ctx['project'] = project
        return ctx
detail = Detail.as_view()


class CreateProject(CreateView):
    model = Project
    fields = ['name', 'description', 'img', 'ong', 'shipping_address']
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(CreateProject, self).get_context_data(**kwargs)
        if self.request.POST:
            context['thing_form'] = ThingFormSet(self.request.POST)
        else:
            context['thing_form'] = ThingFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        thing_form = context['thing_form']
        if thing_form.is_valid():
            self.object = form.save()
            thing_form.instance = self.object
            thing_form.save()
            return redirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))


def donate(request, pk):
    project = get_object_or_404(Project, pk=pk)
    checks = []
    for c in request.GET.getlist('checks[]'):
        checks.append(int(c))
    ships_project = Shipping.objects.filter(project=project, user=request.user)
    for ship_project in ships_project:
        if not ship_project.donations.all():
            break
        ship_project = None
    if not ships_project or not ship_project:
        ship_project = Shipping(project=project, user=request.user)
        ship_project.save()
    ctx = {}
    ctx['project'] = project
    ctx['things_checks'] = checks
    ctx['ship'] = ship_project
    ctx['sendtypes'] = Donation.SENDTYPE
    return render(request, 'project/donate-t1.html', ctx)


def shipping(request, pk):
    if request.POST:
        ship_project = get_object_or_404(Shipping, pk=pk)
        some_donate = False
        donations = []
        for thing in ship_project.project.things.all():
            strid = str(thing.id)
            if request.POST.get('quantity[' + strid + ']') and\
                    int(request.POST.get('quantity[' + strid + ']')) > 0:
                quantity = request.POST.get('quantity[' + strid + ']')
                sendtype = request.POST.get('sendtype[' + strid + ']')
                date = request.POST.get('delivery[' + strid + ']')
                if date:
                    delivery = datetime(int(date[:4]), int(date[5:7]), int(date[8:]))
                else:
                    delivery = None
                donation = Donation(thing=thing, shipping=ship_project,
                        sendtype=sendtype, quantity=quantity, delivery=delivery)
                donation.save()
                donations.append(donation)
                some_donate = True
        if some_donate:
            ship_project.comment = request.POST.get('comment')
            if request.POST.get('show') == 'on':
                ship_project.show = True
            else:
                ship_project.show = False
            ship_project.save()
        ctx = {}
        ctx['ship'] = ship_project
        ctx['donations'] = donations
        ctx['companies'] = ShippingCompany.objects.all()
    return render(request, 'project/shipping.html', ctx)
