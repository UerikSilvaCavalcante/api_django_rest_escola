from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse


class AuthenticateUserTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(
            username="admin", password="admin123", email="admin@xpto"
        )
        self.url = reverse(
            "Estudantes-list"
        )  # Supondo que você tenha uma viewset para Estudante
        self.client_auth = APIClient()

    def test_autenticacao_user_com_credenciais_corretas(self):
        """Teste que verifica a autenticação com credenciais corretas."""
        usuario_autenticado = authenticate(username="admin", password="admin123")
        self.assertTrue(
            (usuario_autenticado is not None) and usuario_autenticado.is_authenticated
        )

    def test_autenticacao_user_com_username_incorreto(self):
        """Teste que verifica a autenticação com username incorreto."""
        usuario_autenticado = authenticate(username="wronguser", password="admin123")
        self.assertIsNone(usuario_autenticado)

    def test_autenticacao_user_com_password_incorreto(self):
        """Teste que verifica a autenticação com password incorreto."""
        usuario_autenticado = authenticate(username="admin", password="wrongpassword")
        self.assertIsNone(usuario_autenticado)

    def test_requisicao_get_autorizada(self):
        """Teste que verifica uma requisição GET autorizada."""

        self.client_auth.force_authenticate(user=self.usuario)
        response = self.client_auth.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # type: ignore

    def test_requisicao_get_nao_autorizada(self):
        """Teste que verifica uma requisição GET não autorizada."""

        response = self.client_auth.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)  # type: ignore
