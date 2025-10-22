from django import forms
from .models import Autor, Editora, Livro

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        exclude = ['id']
        widgets = {
            field: forms.TextInput(attrs={'class': 'form-control'})
            for field in model._meta.fields if field.name != 'id'
        }

class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora
        exclude = ['id']
        widgets = {
            field: forms.TextInput(attrs={'class': 'form-control'})
            for field in model._meta.fields if field.name != 'id'
        }

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        exclude = ['id']
        widgets = {
            field: forms.TextInput(attrs={'class': 'form-control'})
            for field in model._meta.fields if field.name != 'id'
        }
