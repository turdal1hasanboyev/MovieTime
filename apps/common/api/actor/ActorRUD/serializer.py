from rest_framework.serializers import ModelSerializer

from apps.common.models import Actor


class ActorRUDSerializer(ModelSerializer):
    class Meta:
        model = Actor
        fields = (
            'uuid',
            'type',
            "name",
            "created_at",
        )
        
        extra_kwargs = {
            "uuid": {"read_only": True},
            "created_at": {"read_only": True},
        }
        