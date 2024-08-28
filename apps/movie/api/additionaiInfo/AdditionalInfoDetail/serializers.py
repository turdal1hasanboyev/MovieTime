from rest_framework.serializers import ModelSerializer

from apps.movie.models import AdditionalInfo
from apps.movie.api.movie.MovieDetail.serializer import MovieDetailSerializer


class AdditionalInfoDetailSerializer(ModelSerializer):
    movie = MovieDetailSerializer

    class Meta:
        model = AdditionalInfo
        fields = [
            'uuid',
            'movie',
            'key',
            'value',
            "created_at",
        ]
