from django.test import TestCase
from biblioteca.models import Autor
from biblioteca.serializers import AutorSerializer


class AutorSerializerTestCase(TestCase):

    def setUp(self):
        self.autor_data = {
            'nome': 'Machado de Assis'
        }

    def test_serializer_with_valid_data(self):
        serializer = AutorSerializer(data=self.autor_data)
        self.assertTrue(serializer.is_valid())

    def test_serializer_with_invalid_empty_nome(self):
        self.autor_data['nome'] = ''
        serializer = AutorSerializer(data=self.autor_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('nome', serializer.errors)

    def test_serializer_creates_autor(self):
        serializer = AutorSerializer(data=self.autor_data)
        self.assertTrue(serializer.is_valid())
        autor = serializer.save()
        self.assertEqual(autor.nome, 'Machado de Assis')

    def test_serializer_id_is_read_only(self):
        self.autor_data['id'] = 999
        serializer = AutorSerializer(data=self.autor_data)
        self.assertTrue(serializer.is_valid())
        autor = serializer.save()
        self.assertNotEqual(autor.id, 999)
