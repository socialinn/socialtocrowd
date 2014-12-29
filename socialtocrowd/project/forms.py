from django.forms import CharField, Textarea
from django.forms.models import inlineformset_factory
from .models import Project
from .models import Thing
from .models import Direction
import autocomplete_light

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

class ThingSearchForm(autocomplete_light.ModelForm):

    #fields = ['name']
    #widgets = { 'name' : autocomplete_light.TextWidget('AutocompleteThings') }
    # widget=autocomplete_light.TextWidget('AutocompleteUsers')
    name = CharField(label=("Thing name"), max_length=200, required=False, widget=autocomplete_light.TextWidget('AutocompleteThings') )
    #name = autocomplete_light.GenericModelChoiceField('AutocompleteThings')
    #name = autocomplete_light.ModelChoiceField('AutocompleteThings')
    #name = CharField(label=("Cooperativa"), max_length=200, required=False, widget=autocomplete_light.TextWidget('AutocompleteThings'))

    model = Thing

    class Meta:
        model = Thing
        #fields = [ 'name' ]

