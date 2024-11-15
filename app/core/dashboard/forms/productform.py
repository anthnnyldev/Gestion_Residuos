from django import forms
from core.dashboard.models import Product

class ProductForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Descripción del producto'}),
        label='Descripción del producto'
    )

    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'units', 'category', 'is_active']
        labels = {
            'name': 'Nombre del producto',
            'image': 'Imagen del producto',
            'units': 'Unidad de medida',
            'category': 'Categoría',
            'is_active': 'Activo',
        }
