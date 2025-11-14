from django.test import TestCase
from .models import Estudante, Matricula, Curso


# Create your tests here.
class ModelEstudanteTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome="Modelo Teste",
            email="testedemodelo@gmail.com",
            cpf="12345678901",
            data_nascimento="2000-01-01",
            numero="11999999999",
        )

    def test_verifica_atributos_estudante(self):
        self.assertEqual(self.estudante.nome, "Modelo Teste")
        self.assertEqual(self.estudante.email, "testedemodelo@gmail.com")
        self.assertEqual(self.estudante.cpf, "12345678901")
        self.assertEqual(str(self.estudante.data_nascimento), "2000-01-01")
        self.assertEqual(self.estudante.numero, "11999999999")


class ModelCursoTestCase(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(
            codigo="CTM", descricao="Descrição do curso de teste", nivel="B"
        )

    def test_verifica_atributos_curso(self):
        self.assertEqual(self.curso.codigo, "CTM")
        self.assertEqual(self.curso.descricao, "Descrição do curso de teste")
        self.assertEqual(self.curso.nivel, "B")


class ModelMatriculaTestCase(TestCase):
    def setUp(self):
        self.estudante_matricula = Estudante.objects.create(
            nome="Estudante Matricula",
            email="estudantematricula@gmail.com",
            cpf="10987654321",
            data_nascimento="1999-12-31",
            numero="11888888888",
        )
        self.curso_matricula = Curso.objects.create(
            codigo="MTM", descricao="Descrição do curso de matrícula", nivel="I"
        )
        self.matricula = Matricula.objects.create(
            estudante=self.estudante_matricula, curso=self.curso_matricula, periodo="M"
        )

    def test_verifica_atributos_matricula(self):
        self.assertEqual(self.matricula.estudante, self.estudante_matricula)
        self.assertEqual(self.matricula.curso, self.curso_matricula)
        self.assertEqual(self.matricula.periodo, "M")
