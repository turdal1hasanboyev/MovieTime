from rest_framework.serializers import ModelSerializer

from apps.movie.models import Movie


class MovieDestroySerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            'uuid',
            'name',
            'slug',
            'description',
            'genres',
            'awards',
            'actors',
            'regisseurs',
            'category',
            'country',
            'language',
            'views',
            'duration',
            'release_date',
            'trailer',
            "created_at",
        ]
