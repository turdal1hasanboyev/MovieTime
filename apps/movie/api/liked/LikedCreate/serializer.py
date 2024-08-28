from rest_framework.serializers import ModelSerializer

from apps.movie.models import Liked


class LikedCreateSerializer(ModelSerializer):
    class Meta:
        model = Liked
        fields = [
            'uuid',
            'movie',
            'user',
            'like',
            'created_at',
        ]

        extra_kwargs = {
            'uuid': {'read_only': True},
            'created_at': {'read_only': True},
        }
