from rest_framework.serializers import ModelSerializer

from apps.common.models import Category


class CategoryUpdateSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'uuid',
            "name",
            "status",
            "created_at",
        )
        
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
        }
        