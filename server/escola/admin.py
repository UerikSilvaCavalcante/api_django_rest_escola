from django.contrib import admin
from .models import Estudante, Curso, Matricula

# Register your models here.
@admin.register(Estudante)
class EstudanteAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "email", "cpf", "data_nascimento", "numero")
    list_display_links = (
        "id",
        "nome",
    )
    list_per_page = 20
    search_fields = ("nome",)


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("id", "codigo", "descricao", "nivel")
    list_display_links = (
        "id",
        "codigo",
    )
    search_fields = ("codigo",)


@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ("id", "estudante", "curso", "periodo")
    list_display_links = (
        "id",
        "estudante",
    )
    search_fields = ("estudante",)
