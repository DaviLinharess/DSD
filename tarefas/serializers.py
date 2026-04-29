from rest_framework import serializers
from .models import Tarefa
from categorias.models import Categoria

class TarefaSerializer(serializers.HyperlinkedModelSerializer):

    categoria = serializers.HyperlinkedRelatedField(
        view_name='categoria-detail',       # Nome da rota que o router cria no categorias/urls.py
        queryset=Categoria.objects.all()
    )

    class Meta:
        model = Tarefa
        fields = ['url', 'id', 'titulo', 'descricao', 'concluida', 'categoria']

        