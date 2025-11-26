from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Autor, Editora, Livro, Publica

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
        fields = ['nome', 'livro'] 
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome da editora'
            }),
            'livro': forms.Select(attrs={'class': 'form-select'})  
        }


# ---- Formulário Publica (Publicadora) ----
class PublicaForm(forms.ModelForm): 
    class Meta:
        model = Publica
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome da publicadora'
            })
        }


# ---- Formulário Livro ----
class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = [
            'titulo',                
            'isbn',                  
            'publicacao_date',       
            'preco_decimal',         
            'estoque',               
            'editora',              
            'autores',               
        ]
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título do livro'
            }),
            'isbn': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: 9781234567890'
            }),
            'publicacao_date': forms.DateInput(  
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            'preco_decimal': forms.NumberInput(attrs={ 
                'class': 'form-control',
                'step': '0.01',
                'placeholder': 'Ex: 49.90'
            }),
            'estoque': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Quantidade em estoque'
            }),
            'editora': forms.Select(attrs={ 
                'class': 'form-select'
            }),
            'autores': forms.CheckboxSelectMultiple(attrs={  
                'class': 'form-check-input'
            }),
            # OU use SelectMultiple:
            # 'autores': forms.SelectMultiple(attrs={
            #     'class': 'form-select',
            #     'size': '5'
            # }),
        }
        labels = {
            'publicacao_date': 'Data de Publicação',
            'preco_decimal': 'Preço',
            'editora': 'Publicadora',
            'autores': 'Autores',
        }


# ---- Formulário de Cadastro (Sign Up) ----
class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu e-mail'
        })
    )
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu nome'
        })
    )
    last_name = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu sobrenome'
        })
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Escolha um nome de usuário'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Digite sua senha'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirme sua senha'
        })


# ---- Formulário de Login (Sign In) ----
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nome de usuário'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Senha'
        })
    )