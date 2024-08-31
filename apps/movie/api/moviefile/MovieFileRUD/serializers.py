from rest_framework.serializers import ModelSerializer

from apps.movie.models import MovieFile


class MovieFileRUDSerializer(ModelSerializer):
    class Meta:
        model = MovieFile
        fields = [
            'uuid',
            'progressive',
            'movie',
            'file',
            'created_at',
        ]

        extra_kwargs = {
            'uuid': {'read_only': True},
            'created_at': {'read_only': True},
        }
