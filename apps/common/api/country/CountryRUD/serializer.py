from rest_framework.serializers import ModelSerializer

from apps.common.models import Country


class CountryRUDSerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = (
            'uuid',
            "name",
            "created_at",
        )
        
        extra_kwargs = {
            "uuid": {"read_only": True},
            "created_at": {"read_only": True},
        }
        