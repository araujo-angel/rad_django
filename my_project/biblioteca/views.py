from django.shortcuts import render, get_object_or_404, redirect
from .models import Autor, Editora, Livro
from .forms import AutorForm, EditoraForm, LivroForm
from django.shortcuts import render

def base_view(request):
    return render(request, 'biblioteca/base.html')

def dashboard(request):
    return render(request, 'biblioteca/dashboard.html')

# Mapeia entidade → (modelo, form)
MAPEAMENTO = {
    'autor': (Autor, AutorForm),
    'editora': (Editora, EditoraForm),
    'livro': (Livro, LivroForm),
}

def listar_objetos(request, entidade):
    modelo, _ = MAPEAMENTO.get(entidade, (None, None))
    if not modelo:
        return render(request, 'biblioteca/erro.html', {'mensagem': f'Entidade "{entidade}" inválida.'})
    objetos = modelo.objects.all()
    return render(request, 'biblioteca/lista.html', {'objetos': objetos, 'entidade': entidade})

def criar_objeto(request, entidade):
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

def editar_objeto(request, entidade, pk):
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

def deletar_objeto(request, entidade, pk):
    modelo, _ = MAPEAMENTO.get(entidade, (None, None))
    if not modelo:
        return render(request, 'biblioteca/erro.html', {'mensagem': f'Entidade "{entidade}" inválida.'})
    obj = get_object_or_404(modelo, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('listar', entidade=entidade)
    return render(request, 'biblioteca/confirmar_exclusao.html', {'objeto': obj, 'entidade': entidade})
