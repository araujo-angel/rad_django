from django.test import TestCase
from biblioteca.models import Autor


class AutorModelTest(TestCase):

    def setUp(self):
        self.autor = Autor.objects.create(
            nome="Machado de Assis"
        )

    def test_autor_criacao(self):
        self.assertEqual(self.autor.nome, "Machado de Assis")
        self.assertTrue(isinstance(self.autor, Autor))

    def test_autor_str(self):
        self.assertEqual(str(self.autor), self.autor.nome)

    def test_campo_nome_max_length(self):
        self.assertEqual(
            self.autor._meta.get_field('nome').max_length,
            100
        )
