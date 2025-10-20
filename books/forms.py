from django import forms
from .models import Bookshelf 

#forms provide interface for creating & updating data in db
class BookshelfForm(forms.ModelForm):
    class Meta: 
        model = Bookshelf 
        fields = ['title', 'author', 'genre', 'note', 'rating'] #needs to match models.py class