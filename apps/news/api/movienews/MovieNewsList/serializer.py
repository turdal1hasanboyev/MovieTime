from rest_framework.serializers import ModelSerializer

from apps.news.models import MovieNews
from apps.common.api.genre.GenreDetail.serializer import GenreRetrieveSerializer
from apps.common.api.actor.ActorLC.serializer import ActorLCSerializer
from apps.common.api.category.CategoryDetail.serializer import CategoryRetrieveSerializer
from apps.news.api.tag.TagLC.serializer import TagLCSerializer


class MovieNewsListSerializer(ModelSerializer):
    ganres = GenreRetrieveSerializer(many=True)
    regisseurs = ActorLCSerializer(many=True)
    category = CategoryRetrieveSerializer
    actor = ActorLCSerializer(many=True)
    tags = TagLCSerializer(many=True)

    class Meta:
        model = MovieNews
        fields = (
            'uuid',
            "name",
            "slug",
            "description",
            "image",
            "premiere_date",
            "trailer",
            "views",
            "ganres",
            "regisseurs",
            "category",
            "country",
            "actor",
            "tags",
            "created_at",
        )
        