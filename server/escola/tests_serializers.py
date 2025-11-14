from django.test import TestCase
from .models import Estudante, Matricula, Curso
from .serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer


class SerializerEstudanteTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante(
            nome="Serializer Teste",
            email="serializer@teste",
            cpf="12345678901",
            data_nascimento="2000-01-01",
            numero="11999999999",
        )

        self.serializer_estudante = EstudanteSerializer(instance=self.estudante)

    def test_verifica_campos_serializer_estudante(self):
        dados_serializados = self.serializer_estudante.data
        self.assertEqual(
            set(dados_serializados.keys()),  # type: ignore
            set(["id", "nome", "email", "cpf", "data_nascimento", "numero"]),
        )

    def test_verifica_valores_serializer_estudante(self):
        dados_serializados = self.serializer_estudante.data
        self.assertEqual(dados_serializados["nome"], "Serializer Teste")  # type: ignore
        self.assertEqual(dados_serializados["email"], "serializer@teste")  # type: ignore
        self.assertEqual(dados_serializados["cpf"], "12345678901")  # type: ignore
        self.assertEqual(
            dados_serializados["data_nascimento"], "2000-01-01"  # type: ignore
        )
        self.assertEqual(dados_serializados["numero"], "11999999999")  # type: ignore


class SerializerCursoTestCase(TestCase):
    def setUp(self):
        self.curso = Curso(
            codigo="CTMS", descricao="Descrição do curso de teste", nivel="B"
        )

        self.serializer_curso = CursoSerializer(instance=self.curso)

    def test_verifica_campos_serializer_curso(self):
        dados_serializados = self.serializer_curso.data
        self.assertEqual(
            set(dados_serializados.keys()),  # type: ignore
            set(["id", "codigo", "descricao", "nivel"]),
        )

    def test_verifica_valores_serializer_curso(self):
        dados_serializados = self.serializer_curso.data
        self.assertEqual(dados_serializados["codigo"], "CTMS")  # type: ignore
        self.assertEqual(dados_serializados["descricao"], "Descrição do curso de teste")  # type: ignore
        self.assertEqual(dados_serializados["nivel"], "B")  # type: ignore


class SerializerMatriculaTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome="Estudante Matricula",
            email="estudantematricula@gmail.com",
            cpf="10987654321",
            data_nascimento="1999-12-31",
            numero="11888888888",
        )
        self.curso = Curso.objects.create(
            codigo="MTM", descricao="Descrição do curso de matrícula", nivel="I"
        )
        self.matricula = Matricula(
            estudante=self.estudante, curso=self.curso, periodo="M"
        )
        self.serializer_matricula = MatriculaSerializer(instance=self.matricula)

    def test_verifica_campos_serializer_matricula(self):
        dados_serializados = self.serializer_matricula.data
        self.assertEqual(
            set(dados_serializados.keys()),  # type: ignore
            set(["id", "estudante", "curso", "periodo"]),
        )

    def test_verifica_valores_serializer_matricula(self):
        dados_serializados = self.serializer_matricula.data
        self.assertEqual(dados_serializados["estudante"], self.estudante.id)  # type: ignore
        self.assertEqual(dados_serializados["curso"], self.curso.id)  # type: ignore
        self.assertEqual(dados_serializados["periodo"], "M")  # type: ignore
