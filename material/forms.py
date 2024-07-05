from django import forms
from .models import Material

class MaterialForm(forms.ModelForm):
    # Tipos de materiales
    MATERIAL_TYPE_CHOICES = [
        ('Auxiliar', 'Auxiliar'),
        ('Control', 'Control'),
        ('Tutoría', 'Tutoría'),
    ]
    # Años
    YEAR_CHOICES = [(year, year) for year in range(1999, 2024)]

    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'custom-file-input', 'id': 'file-upload'}))
    type = forms.ChoiceField(choices=MATERIAL_TYPE_CHOICES)
    year = forms.ChoiceField(choices=YEAR_CHOICES)

    class Meta:
        model = Material
        fields = ['file', 'name', 'course', 'type', 'year']
