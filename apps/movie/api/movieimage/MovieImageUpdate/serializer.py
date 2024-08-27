from rest_framework.serializers import ModelSerializer

from apps.movie.models import MovieImage


class MovieImageUpdateSerializer(ModelSerializer):
    class Meta:
        model = MovieImage
        fields = [
            'uuid',
            'movie',
            'image',
            'created_at',
        ]

        extra_kwargs = {
            'uuid': {'read_only': True},
            'created_at': {'read_only': True},
        }
