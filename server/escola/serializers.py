from rest_framework import serializers
from .models import Estudante, Curso, Matricula
from .validators import cpf_invalido, nome_invalido, celular_invalido


class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = "__all__"

    def validate(self, attrs):
        if cpf_invalido(attrs["cpf"]):
            raise serializers.ValidationError("CPF inválido")

        if nome_invalido(attrs["nome"]):
            raise serializers.ValidationError("Nome inválido")

        # if celular_invalido(attrs["numero"]):
        #     raise serializers.ValidationError("Número inválido")

        return attrs


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = "__all__"


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = "__all__"


class ListMatriculaEstudanteSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source="curso.descricao")
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ["curso", "periodo"]

    def get_periodo(self, obj):
        return obj.get_periodo_display()


class ListMatriculaCursoSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source="estudante.nome")

    class Meta:
        model = Matricula
        fields = ["estudante_nome"]
