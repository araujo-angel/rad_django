from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'Autor'
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
    
    def __str__(self):
        return self.nome


class Publica(models.Model):
    nome = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'Publica'
        verbose_name = 'Publicadora'
        verbose_name_plural = 'Publicadoras'
    
    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    publicacao_date = models.DateField()
    preco_decimal = models.DecimalField(max_digits=6, decimal_places=2)
    estoque = models.IntegerField()
    
    # Relacionamento Many-to-One com Publica (Editora)
    editora = models.ForeignKey(
        Publica,
        on_delete=models.CASCADE,
        related_name='livros'
    )
    
    # Relacionamento Many-to-Many com Autor
    autores = models.ManyToManyField(
        Autor,
        related_name='livros'
    )
    
    class Meta:
        db_table = 'Livro'
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
    
    def __str__(self):
        return self.titulo


class Editora(models.Model):
    nome = models.CharField(max_length=100)
    
    # Relacionamento One-to-One com Livro
    livro = models.OneToOneField(
        Livro,
        on_delete=models.CASCADE,
        related_name='editora_responsavel'
    )
    
    class Meta:
        db_table = 'Editora'
        verbose_name = 'Editora'
        verbose_name_plural = 'Editoras'
    
    def __str__(self):
        return self.nome