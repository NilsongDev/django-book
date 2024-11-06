# inputbook/forms.py
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'rating']
        labels = {
            'title': 'Titulo',
            'author': 'Autor',
            'rating': 'Valoracion'
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'titulo del libro'}),
            'author': forms.TextInput(attrs={'placeholder': 'nombre de autor'}),
            'rating': forms.NumberInput(attrs={'placeholder': 'valoracion (0 - 10,000)'}),
        }

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating < 0 or rating > 10000:
            raise forms.ValidationError("Rating must be between 0 and 10,000.")
        return rating