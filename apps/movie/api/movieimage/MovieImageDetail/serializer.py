from rest_framework.serializers import ModelSerializer

from apps.movie.models import MovieImage
from apps.movie.api.movie.MovieDetail.serializer import MovieDetailSerializer


class MovieImageRetrieveSerializer(ModelSerializer):
    movie = MovieDetailSerializer

    class Meta:
        model = MovieImage
        fields = [
            'uuid',
            'movie',
            'image',
            'created_at',
        ]
