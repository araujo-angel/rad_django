from django.contrib import admin
from .models import Autor, Editora, Livro, Publica  


# ---- Admin Autor ----
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']  
    search_fields = ['nome']  
    ordering = ['nome']  


# ---- Admin Publica (Publicadora) ----
@admin.register(Publica)  
class PublicaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    search_fields = ['nome']
    ordering = ['nome']


# ---- Admin Editora ----
@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'livro']  
    search_fields = ['nome', 'livro__titulo']  
    list_filter = ['livro']  
    ordering = ['nome']
    
    # Campo de autocomplete para selecionar livro
    autocomplete_fields = ['livro']


# ---- Admin Livro ----
@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = [
        'id', 
        'titulo', 
        'isbn', 
        'editora',  
        'publicacao_date',  
        'preco_decimal',  
        'estoque',
        'mostrar_autores'  
    ]
    
    search_fields = [
        'titulo', 
        'isbn', 
        'autores__nome',  
        'editora__nome'  
    ]
    
    list_filter = [
        'editora',  
        'publicacao_date',  
        'autores'  
    ]
    
    ordering = ['-publicacao_date']  # Mais recentes primeiro
    
    # Campos com autocomplete (busca inteligente)
    autocomplete_fields = ['editora']
    
    # Widget melhorado para ManyToMany (autores)
    filter_horizontal = ['autores'] 
    
    # Organização dos campos no formulário de edição
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('titulo', 'isbn')
        }),
        ('Publicação', {
            'fields': ('editora', 'publicacao_date')
        }),
        ('Autores', {
            'fields': ('autores',),
            'description': 'Selecione um ou mais autores para este livro'
        }),
        ('Comercial', {
            'fields': ('preco_decimal', 'estoque')
        }),
    )
    
    # Método personalizado para exibir autores na listagem
    def mostrar_autores(self, obj):
        """Exibe os autores do livro separados por vírgula"""
        return ", ".join([autor.nome for autor in obj.autores.all()])
    mostrar_autores.short_description = 'Autores'  # Nome da coluna