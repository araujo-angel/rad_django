from django import forms
from .models import Autor, Editora, Livro

# ---- Formulário Autor ----
class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome do autor'
            })
        }


# ---- Formulário Editora ----
class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome da editora'
            })
        }


# ---- Formulário Livro ----
class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = [
            'isbn', 'titulo', 'autor', 'editora',
            'publicacao', 'preco', 'estoque'
        ]
        widgets = {
            'isbn': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: 9781234567890'
            }),
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título do livro'
            }),
            'autor': forms.Select(attrs={'class': 'form-select'}),
            'editora': forms.Select(attrs={'class': 'form-select'}),
            'publicacao': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            'preco': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': 'Ex: 49.90'
            }),
            'estoque': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Quantidade em estoque'
            }),
        }
