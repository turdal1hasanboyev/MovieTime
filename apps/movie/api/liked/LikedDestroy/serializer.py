from rest_framework.serializers import ModelSerializer

from apps.movie.models import Liked


class LikedDestroySerializer(ModelSerializer):
    class Meta:
        model = Liked
        fields = [
            'uuid',
            'movie',
            'user',
            'like',
            'created_at',
        ]
        