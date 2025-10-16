from django import forms 
from .models import Score 

#forms provide interface for creating & updating data in db
class ScoreForm(forms.ModelForm):
    class Meta: 
        model = Score 
        fields = ['name', 'value']