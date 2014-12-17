from django.db import models
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.views.generic.base import View, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.translation import ugettext as _
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.http import HttpResponse, HttpResponseNotFound
import urllib2
import json
from django.contrib.gis.geos import Point

from .forms import ThingFormSet, DirectionFormSet
from .models import Project
from .models import Organization
from .models import Thing, Shipping, Donation
from .models import ShippingCompany
from .models import Direction


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
        query = Project.objects.filter(ong__status="active")
        complexq = Q()
        if q:
            complexq = complexq & Q(name__icontains=q)
            complexq = complexq | Q(description__icontains=q)
            complexq = complexq | Q(ong__name__icontains=q)
            complexq = complexq | Q(ong__description__icontains=q)
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
        query = Organization.objects.filter(status="active")
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

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        messages.add_message(self.request, messages.INFO,
            'Administrators will review the organization as soon as possible')
        return redirect('edit_ong', obj.id)


class UpdateONG(UpdateView):
    model = Organization
    fields = ['name', 'description', 'img', 'city', 'province']
    success_url = '/'

    def get_context_data(self, **kwargs):
        ctx = super(UpdateONG, self).get_context_data(**kwargs)
        ctx['edit'] = True
        return ctx


class ONG(TemplateView):
    template_name = 'project/ong-detail.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super(ONG, self).get_context_data(*args, **kwargs)
        ong = get_object_or_404(Organization, slug=self.kwargs['ongslug'])
        if ong.status == "active" or self.request.user == ong.user:
            ctx['ong'] = ong
        else:
            messages.add_message(self.request, messages.ERROR,
                'Organization deleted or not active')
        return ctx
ong = ONG.as_view()


class Detail(TemplateView):
    template_name = 'project/project-detail.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super(Detail, self).get_context_data(*args, **kwargs)
        project = get_object_or_404(Project, slug=self.kwargs['projectslug'])
        ctx['project'] = project
        return ctx
detail = Detail.as_view()


class CreateProject(CreateView):
    model = Project
    fields = ['name', 'description', 'img']

    def get_context_data(self, *args, **kwargs):
        context = super(CreateProject, self).get_context_data(*args, **kwargs)
        ong = get_object_or_404(Organization, slug=self.kwargs['ongslug'])
        if (self.request.user != ong.user):
            messages.add_message(self.request, messages.ERROR,
                'Insufficient permissions')
        context['ong'] = ong
        if self.request.POST:
            context['thing_form'] = ThingFormSet(self.request.POST)
            context['direction_form'] = DirectionFormSet(self.request.POST)
        else:
            context['thing_form'] = ThingFormSet()
            context['direction_form'] = DirectionFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        obj = form.save(commit=False)
        obj.ong = context['ong']
        obj.save()
        thing_form = context['thing_form']
        direction_form = context['direction_form']
        if thing_form.is_valid() and direction_form.is_valid():
            self.object = form.save()
            thing_form.instance = self.object
            thing_form.save()
            direction_form.instance = self.object
            direction_form.save()
            messages.add_message(self.request, messages.INFO,
                'Project created successful')
            return redirect('detail', obj.id)
        else:
            return self.render_to_response(self.get_context_data(form=form))


class UpdateProject(UpdateView):
    model = Project
    fields = ['name', 'description', 'img', 'twitter', 'googleplus', 'facebook' ]
    success_url = '/'

    def get_object(self):
        return Project.objects.get(slug=self.kwargs['projectslug'])

    def get_context_data(self, *args, **kwargs):
        context = super(UpdateProject, self).get_context_data(*args, **kwargs)
        context['edit'] = True
        return context


class CreateThing(CreateView):
    model = Thing
    fields = ['name', 'description', 'quantity']

    def get_context_data(self, *args, **kwargs):
        context = super(CreateThing, self).get_context_data(*args, **kwargs)
        project = get_object_or_404(Project, pk=self.args[0])
        if (self.request.user != project.ong.user):
            messages.add_message(self.request, messages.ERROR,
                'Insufficient permissions')
        context['project'] = project
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        obj = form.save(commit=False)
        obj.project = context['project']
        obj.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        context = self.get_context_data()
        return reverse('edit_project', kwargs={ 'projectslug' : context['project'].getslug() })


class UpdateThing(UpdateView):
    model = Thing
    fields = ['name', 'description', 'quantity']

    def get_context_data(self, **kwargs):
        ctx = super(UpdateThing, self).get_context_data(**kwargs)
        ctx['edit'] = True
        return ctx

    def get_success_url(self):
        context = self.get_context_data()
        return reverse('edit_project', kwargs={ 'projectslug' : context['thing'].project.getslug() })


class RemoveThing(DeleteView):
    model = Thing
    fields = ['name', 'description', 'quantity']

    def get_context_data(self, **kwargs):
        ctx = super(RemoveThing, self).get_context_data(**kwargs)
        ctx['edit'] = True
        return ctx

    def get_success_url(self):
        context = self.get_context_data()
        return reverse('edit_project', kwargs={ 'projectslug' : context['thing'].project.getslug() })


class CreateDirection(CreateView):
    model = Direction
    fields = ['description', 'timetable', 'phone', 'pos']

    def get_context_data(self, *args, **kwargs):
        context = super(CreateDirection, self).get_context_data(*args, **kwargs)
        project = get_object_or_404(Project, pk=self.args[0])
        if (self.request.user != project.ong.user):
            messages.add_message(self.request, messages.ERROR,
                'Insufficient permissions')
        context['project'] = project
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        obj = form.save(commit=False)
        obj.project = context['project']
        obj.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        context = self.get_context_data()
        return reverse('edit_project', kwargs={ 'projectslug' : context['project'].getslug(), })


class UpdateDirection(UpdateView):
    model = Direction
    fields = ['description', 'timetable', 'phone', 'pos']

    def get_context_data(self, **kwargs):
        ctx = super(UpdateDirection, self).get_context_data(**kwargs)
        ctx['edit'] = True
        return ctx

    def get_success_url(self):
        context = self.get_context_data()
        return reverse('edit_project', kwargs={ 'projectslug' : context['direction'].project.getslug(), })


class RemoveDirection(DeleteView):
    model = Direction
    fields = ['description', 'pos', 'timetable', 'phone']

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['edit'] = True
        return ctx

    def get_success_url(self):
        context = self.get_context_data()
        return reverse('edit_project', kwargs={ 'projectslug' : context['direction'].project.getslug(), })


@login_required
def donate(request, projectslug):
    if not request.POST:
        return

    ctx = {}
    # Create/edit shipping for donate
    project = get_object_or_404(Project, slug=projectslug)
    ships_project = Shipping.objects.filter(project=project, user=request.user,
            status='creating')
    if ships_project:
        ship_project = ships_project[0]
    else:
        ship_project = Shipping(project=project, user=request.user, status='creating')
        ship_project.save()

    # Add donate
    thing = get_object_or_404(Thing, id=request.POST.get('thing_id'))
    info = request.POST.get('info')
    quantity = request.POST.get('quantity')
    img = request.POST.get('img')
    donation = Donation(thing=thing, shipping=ship_project, info=info,
            quantity=quantity, img=img)
    donation.save()

    # Close shipping
    if (request.POST.get('close')):
        ship_project.status = 'sent'
        ship_project.show = request.POST.get('show')
        ctx['close'] = True
        ship_project.save()

    ctx['project'] = project
    ctx['ship'] = ship_project
    return redirect(request.META.get('HTTP_REFERER'))


def addr_to_url(addr):
    return "http://nominatim.openstreetmap.org/?format=json&addressdetails=1&q=" + addr.strip().replace(" ", "+") + "&format=json&limit=1"

def addr_to_geo(addr):
    url = addr_to_url(addr)
    jsonreq = urllib2.urlopen(url.encode('UTF-8')).read()
    data = json.loads(jsonreq)
    return { key : data[0][key] for key in { "lat", "lon" } }

class NearProject(TemplateView):
    template_name = 'project/near.html'
    def get_context_data(self, *args, **kwargs):
        ctx = super(NearProject, self).get_context_data(*args, **kwargs)
        print(self.kwargs['projectslug'])
        ctx['selected_project'] = self.kwargs['projectslug']
        return ctx
nearproject = NearProject.as_view()

class DoNearView(View):

    def post(self, request):
        addr = request.POST.get('address')
        selected_project = request.POST.get('project')
        geoaddr = addr_to_geo(addr)
        json_data = {}
        json_data['geoaddr'] = [ float(geoaddr['lon']), float(geoaddr['lat']) ]
        alldirs = []
        print("selproj: " + selected_project)
        if selected_project == "":
            projects = Project.objects.all()
        else:
            projects = Project.objects.filter(slug=selected_project)

        for proj in projects:
            punto = Point(float(geoaddr['lon']), float(geoaddr['lat']))
            dirs = [ { 'pos' : [thedir.pos.x, thedir.pos.y], 'project' : proj.__str__() } for thedir in proj.directions.filter(pos__distance_lt=(punto, 500000)) ]
            alldirs = alldirs + dirs
        print(alldirs)
        json_data['neardirs'] = alldirs
        return HttpResponse(json.dumps(json_data), content_type="application/json")

donear = DoNearView.as_view()
