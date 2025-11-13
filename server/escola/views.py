from rest_framework import viewsets, generics, filters
from .models import Estudante, Curso, Matricula
from .serializers import (
    EstudanteSerializer,
    CursoSerializer,
    MatriculaSerializer,
    ListMatriculaCursoSerializer,
    ListMatriculaEstudanteSerializer,
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class EstudanteViewSet(viewsets.ModelViewSet):
    """
    Descrição da ViewSet:
    - Endpoint para CRUD de estudantes.

    Campos de ordenação:
    - nome: permite ordenar os resultados por nome.

    Campos de pesquisa:
    - nome: permite pesquisar os resultados por nome.
    - cpf: permite pesquisar os resultados por CPF.

    Métodos HTTP Permitidos:
    - GET, POST, PUT, PATCH, DELETE

    Classe de Serializer:
    - EstudanteSerializer: usado para serialização e desserialização de dados.
    - Se a versão da API for 'v2', usa EstudanteSerializerV2.
    """

    queryset = Estudante.objects.all().order_by("id")
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["nome"]
    search_fields = ["nome", "cpf"]

    def get_serializer_class(self):  # type: ignore
        return EstudanteSerializer


class CursoViewSet(viewsets.ModelViewSet):
    """
    Descrição da ViewSet:
    - Endpoint para CRUD de cursos.

    Métodos HTTP Permitidos:
    - GET, POST, PUT, PATCH, DELETE
    """

    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Curso.objects.all().order_by("id")
    serializer_class = CursoSerializer


class MatriculaAnonRateThrottle(AnonRateThrottle):
    rate = "5/day"


class MatriculaViewSet(viewsets.ModelViewSet):
    """
    Descrição da ViewSet:
    - Endpoint para CRUD de matrículas.

    Métodos HTTP Permitidos:
    - GET, POST

    Throttle Classes:
    - MatriculaAnonRateThrottle: limite de taxa para usuários anônimos.
    - UserRateThrottle: limite de taxa para usuários autenticados.
    """

    queryset = Matricula.objects.all().order_by("id")
    serializer_class = MatriculaSerializer
    throttle_classes = [UserRateThrottle, MatriculaAnonRateThrottle]
    http_method_names = ["get", "post"]


class ListMatriculaEstudante(generics.ListAPIView):
    """
    Descrição da View:
    - Lista Matriculas por id de Estudante
    Parâmetros:
    - pk (int): O identificador primário do objeto. Deve ser um número inteiro.
    """

    def get_queryset(self):  # type: ignore
        queryset = Matricula.objects.filter(estudante_id=self.kwargs["pk"]).order_by(
            "id"
        )
        return queryset

    serializer_class = ListMatriculaEstudanteSerializer


class ListMatriculaCurso(generics.ListAPIView):
    """
    Descrição da View:
    - Lista Matriculas por id de Curso
    Parâmetros:
    - pk (int): O identificador primário do objeto. Deve ser um número inteiro.
    """

    def get_queryset(self):  # type: ignore
        queryset = Matricula.objects.filter(curso_id=self.kwargs["pk"]).order_by("id")
        return queryset

    serializer_class = ListMatriculaCursoSerializer
