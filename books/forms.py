from django import forms
from .models import Bookshelf 

#forms provide interface for creating & updating data in db
class BookshelfForm(forms.ModelForm):
    class Meta: 
        model = Bookshelf 
        fields = ['title', 'author', 'genre', 'note', 'rating'] #needs to match models.py class
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter title',}),
            'author': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter author\'s name',}),
            'note': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Optional: Enter notes',}),
            'rating': forms.NumberInput(attrs={'type': 'range', 'min':0, 'max':11})
        }