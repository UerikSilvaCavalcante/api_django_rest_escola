from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from .models import Matricula, Estudante, Curso
from .serializers import MatriculaSerializer
from rest_framework import status


class MatriculasTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(
            username="testuser", password="testpass", email="testuser@xpto"
        )
        self.url = reverse("Matriculas-list")
        self.client_auth = APIClient()
        self.client_auth.force_authenticate(user=self.usuario)
        self.estudante = Estudante.objects.create(
            nome="Teste estudante",
            email="testeestudante@gmail.com",
            cpf="68224431002",
            data_nascimento="2024-01-02",
            numero="86 99999-9999",
        )
        self.curso = Curso.objects.create(
            codigo="CURS001", descricao="Curso de Teste", nivel="B"
        )
        self.matricula_01 = Matricula.objects.create(
            estudante=self.estudante, curso=self.curso, periodo="M"
        )

    def test_get_matriculas(self):
        """Teste para obter a lista de matrículas."""
        response = self.client_auth.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # type: ignore

    def test_get_matricula_by_pk(self):
        """Teste para obter uma matrícula específica pelo PK"""
        response = self.client_auth.get(f"{self.url}1/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # type: ignore
        dados_matricula = Matricula.objects.get(pk=1)
        serializer = MatriculaSerializer(dados_matricula)
        self.assertEqual(response.data, serializer.data)  # type: ignore

    def test_create_matricula(self):
        """Teste para criar uma matrícula com dados válidos."""
        new_matricula = {
            "estudante": self.estudante.pk,
            "curso": self.curso.pk,
            "periodo": "V",
        }
        response = self.client_auth.post(self.url, data=new_matricula)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # type: ignore

    def test_delete_matricula(self):
        """Teste para deletar uma matrícula existente."""
        response = self.client_auth.delete(f"{self.url}1/")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)  # type: ignore

    def test_update_matricula(self):
        """Teste para atualizar uma matrícula existente."""
        updated_matricula = {
            "estudante": self.estudante.pk,
            "curso": self.curso.pk,
            "periodo": "N",
        }
        response = self.client_auth.put(f"{self.url}1/", data=updated_matricula)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)  # type: ignore
