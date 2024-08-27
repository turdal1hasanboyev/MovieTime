from rest_framework.serializers import ModelSerializer

from apps.movie.models import MovieImage


class MovieImageDestroySerializer(ModelSerializer):
    class Meta:
        model = MovieImage
        fields = [
            'uuid',
            'movie',
            'image',
            'created_at',
        ]
        