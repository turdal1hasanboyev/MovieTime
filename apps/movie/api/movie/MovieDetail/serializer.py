from rest_framework.serializers import ModelSerializer

from apps.movie.models import Movie
from apps.common.api.genre.GenreDetail.serializer import GenreRetrieveSerializer
from apps.common.api.award.AwardLC.serializer import AwardLCSerializer
from apps.common.api.actor.ActorLC.serializer import ActorLCSerializer
from apps.common.api.category.CategoryDetail.serializer import CategoryRetrieveSerializer
from apps.common.api.country.CountryList.serializer import CountryListSerializer


class MovieDetailSerializer(ModelSerializer):
    genres = GenreRetrieveSerializer(many=True)
    awards = AwardLCSerializer(many=True)
    actors = ActorLCSerializer(many=True)
    regisseurs = ActorLCSerializer(many=True)
    category = CategoryRetrieveSerializer
    country = CountryListSerializer

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
