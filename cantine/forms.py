from django import forms
from cantine.models.plat_model import Plat

class PlatForm(forms.ModelForm):
    class Meta:
        model = Plat
        fields = ['name', 'summary']
        labels = {'name': 'Nom du plat', 'summary': 'Description du plat'}
        
        widgets = {
            'name': forms.TextInput(attrs={}),
            'summary': forms.Textarea(attrs={})
            
        }