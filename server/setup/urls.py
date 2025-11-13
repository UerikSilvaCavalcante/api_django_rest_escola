from django.contrib import admin
from django.urls import path, include
from escola.urls import router
from escola.views import ListMatriculaEstudante, ListMatriculaCurso
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Documentação API",
        default_version="v1",
        description="Documentação da API da Escola",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="uerik@xpto.com.br"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("estudantes/<int:pk>/matriculas/", ListMatriculaEstudante.as_view()),
    path("cursos/<int:pk>/matriculas/", ListMatriculaCurso.as_view()),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
