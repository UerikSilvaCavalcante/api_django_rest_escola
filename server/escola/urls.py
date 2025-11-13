from django.urls import path
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register("estudantes", EstudanteViewSet, basename="Estudantes")
router.register("cursos", CursoViewSet, basename="Cursos")
router.register("matriculas", MatriculaViewSet, basename="Matriculas")

