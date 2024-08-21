from rest_framework.serializers import ModelSerializer

from apps.news.models import Tag


class TagLCSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'uuid',
            "name",
            "created_at",
        )

        extra_kwargs = {
            "uuid": {"read_only": True},
            "created_at": {"read_only": True},
        }
        