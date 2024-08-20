from rest_framework.serializers import ModelSerializer

from apps.common.models import Category


class CategoryDestroySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'uuid',
            "name",
            "status",
            "created_at",
        )
        