from rest_framework.serializers import ModelSerializer

from apps.news.models import MovieNews


class MovieNewsDestroySerializer(ModelSerializer):
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
        