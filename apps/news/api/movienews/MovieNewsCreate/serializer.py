from rest_framework.serializers import ModelSerializer

from apps.news.models import MovieNews


class MovieNewsCreateSerializer(ModelSerializer):
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
        
        extra_kwargs = {
            "uuid": {"read_only": True},
            "created_at": {"read_only": True},
        }
        