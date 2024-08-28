from rest_framework.serializers import ModelSerializer

from apps.movie.models import AdditionalInfo


class AdditionalInfoCreateSerializer(ModelSerializer):
    class Meta:
        model = AdditionalInfo
        fields = [
            "uuid",
            'movie',
            'key',
            'value',
            "created_at",
        ]

    extra_kwargs = {
        "uuid": {"read_only": True},
        "created_at": {"read_only": True},
    }
    