from django import forms
from .models import Farm, Tillage, Harvest


class FarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = ['name', 'geolocalization']

class HarvestForm(forms.ModelForm):
    class Meta:
        model = Harvest
        fields = ['name','localization']