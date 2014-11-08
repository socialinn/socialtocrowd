from django.forms import Textarea
from django.forms.models import inlineformset_factory
from .models import Project
from .models import Thing


TOTAL_THINGS_NEW_PROJECT = 10

ThingFormSet = inlineformset_factory(Project, Thing, min_num=1,
        max_num=TOTAL_THINGS_NEW_PROJECT, validate_min=True,
        extra=TOTAL_THINGS_NEW_PROJECT, can_delete=False,
        widgets = { 'description': Textarea(attrs={'cols': 50, 'rows': 3}) },
        fields=('name', 'quantity', 'description')
)
