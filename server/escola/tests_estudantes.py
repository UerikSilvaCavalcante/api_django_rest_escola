from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status
from .models import Estudante
from .serializers import EstudanteSerializer


class EstudantesTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(
            username="testuser", password="testpass", email="testuser@xpto"
        )
        self.url = reverse("Estudantes-list")
        self.client_auth = APIClient()
        self.client_auth.force_authenticate(user=self.usuario)
        self.estudante_01 = Estudante.objects.create(
            nome="Teste estudante UM",
            email="testeestudante01@gmail.com",
            cpf="68224431002",
            data_nascimento="2024-01-02",
            numero="3849732483",
        )
        self.estudante_02 = Estudante.objects.create(
            nome="Teste estudante DOIS",
            email="testeestudante02@gmail.com",
            cpf="70261486055",
            data_nascimento="2024-01-02",
            numero="3849732483",
        )

    def test_get_estudantes(self):
        """Teste para obter a lista de estudantes."""
        response = self.client_auth.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # type: ignore

    def test_get_estudante_by_pk(self):
        """Teste para obter um estudante específico pelo PK"""
        response = self.client_auth.get(f"{self.url}1/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # type: ignore
        dados_estudante = Estudante.objects.get(pk=1)
        serializer = EstudanteSerializer(dados_estudante)
        self.assertEqual(response.data, serializer.data)  # type: ignore

    def test_create_estudante(self):
        """Teste para criar um estudante com dados válidos."""
        data = {
            "nome": "Teste estudante TRES",
            "email": "testeestudante03@gmail.com",
            "cpf": "12345678909",
            "data_nascimento": "2024-01-02",
            "numero": "3849732483",
        }

        response = self.client_auth.post(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # type: ignore

    def test_delete_estudante(self):
        """Teste para deletar um estudante existente."""
        response = self.client_auth.delete(f"{self.url}2/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)  # type: ignore

    def test_update_estudante(self):
        """Teste para atualizar os dados de um estudante existente."""
        estudante_atualizado = {
            "nome": "Teste estudante UM atualizado",
            "email": "testeestudante01atualizado@gmail.com",
            "cpf": "68224431202",
            "data_nascimento": "2024-01-02",
            "numero": "3849732483",
        }
        response = self.client_auth.put(f"{self.url}1/", data=estudante_atualizado)
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # type: ignore
