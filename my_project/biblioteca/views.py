from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .models import Autor, Editora, Livro
from .forms import AutorForm, EditoraForm, LivroForm, SignUpForm, LoginForm
from django.core.paginator import Paginator
from django.core.exceptions import PermissionDenied
def base_view(request):
    return render(request, 'biblioteca/base.html')

@login_required
def dashboard(request):
    return render(request, 'biblioteca/dashboard.html')

# Mapeia entidade → (modelo, form)
MAPEAMENTO = {
    'autor': (Autor, AutorForm),
    'editora': (Editora, EditoraForm),
    'livro': (Livro, LivroForm),
}

@login_required
def listar_objetos(request, entidade):
    modelo, _ = MAPEAMENTO.get(entidade, (None, None))
    if not modelo:
        return render(request, 'biblioteca/erro.html', {'mensagem': f'Entidade "{entidade}" inválida.'})
    objetos = modelo.objects.all()

    # Paginação: 10 itens por página
    paginator = Paginator(objetos, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'biblioteca/lista.html', {'objetos': page_obj, 'entidade': entidade, 'page_obj': page_obj})

@login_required
def criar_objeto(request, entidade):
    # Verificar permissão para livros
    if entidade == 'livro' and not request.user.has_perm('biblioteca.add_livro'):
        raise PermissionDenied("Você não tem permissão para criar livros.")

    _, Form = MAPEAMENTO.get(entidade, (None, None))
    if not Form:
        return render(request, 'biblioteca/erro.html', {'mensagem': f'Entidade "{entidade}" inválida.'})

    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar', entidade=entidade)
    else:
        form = Form()

    return render(request, 'biblioteca/form.html', {'form': form, 'entidade': entidade})

@login_required
def editar_objeto(request, entidade, pk):
    # Verificar permissão para livros
    if entidade == 'livro' and not request.user.has_perm('biblioteca.change_livro'):
        raise PermissionDenied("Você não tem permissão para editar livros.")

    modelo, Form = MAPEAMENTO.get(entidade, (None, None))
    if not modelo:
        return render(request, 'biblioteca/erro.html', {'mensagem': f'Entidade "{entidade}" inválida.'})
    obj = get_object_or_404(modelo, pk=pk)
    if request.method == 'POST':
        form = Form(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('listar', entidade=entidade)
    else:
        form = Form(instance=obj)
    return render(request, 'biblioteca/form.html', {'form': form, 'entidade': entidade})

@login_required
def deletar_objeto(request, entidade, pk):
    # Verificar permissão para livros
    if entidade == 'livro' and not request.user.has_perm('biblioteca.delete_livro'):
        raise PermissionDenied("Você não tem permissão para deletar livros.")

    modelo, _ = MAPEAMENTO.get(entidade, (None, None))
    if not modelo:
        return render(request, 'biblioteca/erro.html', {'mensagem': f'Entidade "{entidade}" inválida.'})
    obj = get_object_or_404(modelo, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('listar', entidade=entidade)
    return render(request, 'biblioteca/confirmar_exclusao.html', {'objeto': obj, 'entidade': entidade})


# ---- Views de Autenticação ----

def signup_view(request):
    """View para cadastro de novos usuários"""
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Bem-vindo, {user.first_name}! Sua conta foi criada com sucesso.')
            return redirect('dashboard')
    else:
        form = SignUpForm()

    return render(request, 'biblioteca/signup.html', {'form': form})


def login_view(request):
    """View para login de usuários"""
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bem-vindo de volta, {user.first_name or user.username}!')
                next_url = request.GET.get('next', 'dashboard')
                return redirect(next_url)
    else:
        form = LoginForm()

    return render(request, 'biblioteca/login.html', {'form': form})


@login_required
def logout_view(request):
    """View para logout de usuários"""
    logout(request)
    messages.info(request, 'Você saiu da sua conta com sucesso.')
    return redirect('login')


# ---- Handler para erro de permissão ----

def permission_denied_view(request, exception=None):
    """View customizada para erro 403 - Permissão Negada"""
    return render(request, 'biblioteca/403.html', status=403)
