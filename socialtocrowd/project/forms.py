from django.forms import Textarea
from django.forms.models import inlineformset_factory
from .models import Project
from .models import Thing
from .models import Direction


TOTAL_THINGS_NEW_PROJECT = 20

ThingFormSet = inlineformset_factory(Project, Thing, min_num=1,
        max_num=TOTAL_THINGS_NEW_PROJECT, validate_min=True,
        extra=0, can_delete=False,
        widgets = { 'description': Textarea(attrs={'cols': 50, 'rows': 3}) },
        fields=('name', 'quantity', 'description')
)

DirectionFormSet = inlineformset_factory(Project, Direction, min_num=1,
        max_num=1, validate_min=True, extra=1, can_delete=False,
        fields=('description', 'pos', 'timetable', 'phone')
)
