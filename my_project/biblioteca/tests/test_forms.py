from django.test import TestCase
from biblioteca.forms import AutorForm
from biblioteca.models import Autor


class AutorFormTest(TestCase):

    def test_autor_form_valid(self):
        form_data = {'nome': 'Machado de Assis'}
        form = AutorForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_autor_form_invalid_empty_nome(self):
        form_data = {'nome': ''}
        form = AutorForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('nome', form.errors)

    def test_autor_form_no_data(self):
        form = AutorForm()
        self.assertFalse(form.is_valid())

    def test_autor_form_save(self):
        form_data = {'nome': 'Clarice Lispector'}
        form = AutorForm(data=form_data)
        self.assertTrue(form.is_valid())
        autor = form.save()
        self.assertEqual(autor.nome, 'Clarice Lispector')
        self.assertTrue(Autor.objects.filter(nome='Clarice Lispector').exists())
