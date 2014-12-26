
import autocomplete_light
from .models import Thing

class AutocompleteThings(autocomplete_light.AutocompleteGenericBase):
    choices = (
        Thing.objects.all(),
    )

    search_fields = (('name',),)
    model = Thing
    limit_choices = 5

autocomplete_light.register(AutocompleteThings)
