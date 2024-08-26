from rest_framework.serializers import ModelSerializer

from apps.common.models import Country


class CountryListSerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = (
            'uuid',
            "name",
            "created_at",
        )
        