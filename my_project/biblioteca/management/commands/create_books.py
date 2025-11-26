from django.core.management.base import BaseCommand
from biblioteca.models import Livro, Autor, Publica
from faker import Faker
import random


class Command(BaseCommand):
    help = 'Gera 100 registros de livros no banco de dados usando Faker'

    def handle(self, *args, **kwargs):
        fake = Faker('pt_BR')  # Usando locale brasileiro

        self.stdout.write(self.style.SUCCESS('Iniciando geração de livros...'))

        # Primeiro, vamos criar alguns autores e editoras se não existirem
        autores_list = []
        if Autor.objects.count() < 20:
            self.stdout.write('Criando autores...')
            for _ in range(20):
                autor = Autor.objects.create(
                    nome=fake.name()
                )
                autores_list.append(autor)
            self.stdout.write(self.style.SUCCESS(f'Criados {len(autores_list)} autores'))
        else:
            autores_list = list(Autor.objects.all())

        editoras_list = []
        if Publica.objects.count() < 10:
            self.stdout.write('Criando editoras...')
            for _ in range(10):
                editora = Publica.objects.create(
                    nome=fake.company()
                )
                editoras_list.append(editora)
            self.stdout.write(self.style.SUCCESS(f'Criadas {len(editoras_list)} editoras'))
        else:
            editoras_list = list(Publica.objects.all())

        # Agora vamos criar 100 livros
        self.stdout.write('Criando livros...')
        livros_criados = 0
        tentativas = 0
        max_tentativas = 200  # Para evitar loop infinito em caso de ISBNs duplicados

        while livros_criados < 100 and tentativas < max_tentativas:
            tentativas += 1

            try:
                # Gerar ISBN único (usando isbn13)
                isbn = fake.isbn13(separator="")

                # Criar o livro
                livro = Livro.objects.create(
                    titulo=fake.sentence(nb_words=random.randint(2, 6)).rstrip('.'),
                    isbn=isbn,
                    publicacao_date=fake.date_between(start_date='-30y', end_date='today'),
                    preco_decimal=round(random.uniform(15.00, 150.00), 2),
                    estoque=random.randint(0, 100),
                    editora=random.choice(editoras_list)
                )

                # Adicionar de 1 a 3 autores aleatórios ao livro
                numero_autores = random.randint(1, 3)
                autores_selecionados = random.sample(autores_list, numero_autores)
                livro.autores.set(autores_selecionados)

                livros_criados += 1

                if livros_criados % 10 == 0:
                    self.stdout.write(f'Criados {livros_criados} livros...')

            except Exception as e:
                # Se o ISBN já existe, tenta novamente
                continue

        if livros_criados == 100:
            self.stdout.write(self.style.SUCCESS(f'\nSucesso! {livros_criados} livros foram criados no banco de dados.'))
        else:
            self.stdout.write(self.style.WARNING(f'\nAviso: Apenas {livros_criados} livros foram criados após {tentativas} tentativas.'))