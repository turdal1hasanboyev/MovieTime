from rest_framework.serializers import ModelSerializer

from apps.movie.models import Movie


class MovieCreateSerializer(ModelSerializer):
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

        extra_kwargs = {
            'uuid': {'read_only': True},
            'created_at': {'read_only': True},
        }
