from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from biblioteca.models import Autor


class AutorAPITestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def test_list_autores(self):
        response = self.client.get('/biblioteca/api/autores/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_autor(self):
        autor = Autor.objects.create(nome='Machado de Assis')
        response = self.client.get(f'/biblioteca/api/autores/{autor.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_autor(self):
        data = {
            "nome": "Clarice Lispector"
        }
        response = self.client.post('/biblioteca/api/autores/', data, format='json')
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
