from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from biblioteca.models import Autor


class ListAutoresViewTest(TestCase):

    def setUp(self):
        self.client = Client()

        # Usuário para autenticação (login_required)
        self.user = User.objects.create_user(
            username='teste',
            password='12345'
        )
        self.client.login(username='teste', password='12345')

        # URL dinâmica da listagem de autores
        self.url = reverse('listar', kwargs={'entidade': 'autor'})

        # Criar autores de teste (mais de 10 para testar paginação)
        for i in range(12):
            Autor.objects.create(nome=f'Autor {i}')

    def test_list_autores_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_list_autores_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'biblioteca/lista.html')

    def test_list_autores_context(self):
        response = self.client.get(self.url)
        self.assertIn('objetos', response.context)
        self.assertIn('page_obj', response.context)

    def test_list_autores_pagination_first_page(self):
        response = self.client.get(self.url)
        autores = response.context['objetos']
        self.assertEqual(len(autores), 10)

    def test_list_autores_second_page(self):
        response = self.client.get(self.url + '?page=2')
        autores = response.context['objetos']
        self.assertEqual(len(autores), 2)

    def test_list_autores_invalid_page(self):
        response = self.client.get(self.url + '?page=invalid')
        autores = response.context['objetos']
        self.assertEqual(len(autores), 10)

    def test_list_autores_order(self):
        response = self.client.get(self.url)
        autores = response.context['objetos']
        self.assertEqual(autores[0].nome, 'Autor 0')
