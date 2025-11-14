from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from .models import Curso
from .serializers import CursoSerializer
from rest_framework import status


class CursosTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(
            username="testuser", password="testpass", email="testuser@xpto"
        )
        self.url = reverse("Cursos-list")
        self.client_auth = APIClient()
        self.client_auth.force_authenticate(user=self.usuario)
        self.curso_01 = Curso.objects.create(
            codigo="CURS001", descricao="Curso de Teste Um", nivel="B"
        )
        self.curso_02 = Curso.objects.create(
            codigo="CURS002", descricao="Curso de Teste Dois", nivel="I"
        )

    def test_get_cursos(self):
        """Teste para obter a lista de cursos."""
        response = self.client_auth.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK) # type: ignore

    def test_get_curso_by_pk(self):
        """Teste para obter um curso específico pelo PK"""
        response = self.client_auth.get(f"{self.url}1/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK) # type: ignore
        dados_curso = Curso.objects.get(pk=1)
        serializer = CursoSerializer(dados_curso)
        self.assertEqual(response.data, serializer.data)  # type: ignore

    def test_create_curso(self):
        """Teste para criar um curso com dados válidos."""
        new_curso = {
            "codigo": "CURS003",
            "descricao": "Curso de Teste Tres",
            "nivel": "A",
        }
        response = self.client_auth.post(self.url, data=new_curso)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) # type: ignore

    def test_delete_curso(self):
        """Teste para deletar um curso existente."""
        response = self.client_auth.delete(f"{self.url}2/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT) # type: ignore

    def test_create_curso_invalid_codigo(self):
        """Teste para criar um curso com código inválido (menos de 4 caracteres)."""
        new_curso = {
            "codigo": "C1",
            "descricao": "Curso Inválido",
            "nivel": "B",
        }
        response = self.client_auth.post(self.url, data=new_curso)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST) # type: ignore

    def test_put_curso(self):
        """Teste para atualizar um curso existente."""
        updated_curso = {
            "codigo": "CURS001",
            "descricao": "Curso de Teste Um Atualizado",
            "nivel": "I",
        }
        response = self.client_auth.put(f"{self.url}1/", data=updated_curso)
        self.assertEqual(response.status_code, status.HTTP_200_OK) # type: ignore
        curso = Curso.objects.get(pk=1)
        self.assertEqual(curso.descricao, "Curso de Teste Um Atualizado")
        self.assertEqual(curso.nivel, "I")
