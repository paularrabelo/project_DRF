from rest_framework import serializers

from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'post',
            'active',
        )


class CursoSerializer(serializers.ModelSerializer):
    #Nested Relationship
    #avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    
    #HyperLinked Related Field
    avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'post',
            'active',
            'avaliacoes'
        )