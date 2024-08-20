from rest_framework.serializers import ModelSerializer

from apps.common.models import Award


class AwardRUDSerializer(ModelSerializer):
    class Meta:
        model = Award
        fields = (
            'uuid',
            'date',
            "name",
            "created_at",
        )
        
        extra_kwargs = {
            "uuid": {"read_only": True},
            "created_at": {"read_only": True},
        }
        