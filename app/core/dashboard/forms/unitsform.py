from django import forms
from core.dashboard.models import Units

class UnitsForm(forms.ModelForm):
    class Meta:
        model = Units
        fields = ['name', 'abbreviation']
        labels = {
            'name': 'Nombre de unidad',
            'abbreviation': 'Abreviación de unidad',
        }
