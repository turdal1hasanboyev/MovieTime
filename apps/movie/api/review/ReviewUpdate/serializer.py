from rest_framework.serializers import ModelSerializer

from apps.movie.models import Review


class ReviewUpdateSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'uuid',
            'movie',
            'user',
            'rate',
            'review',
            'created_at',
        ]

        extra_kwargs = {
            'uuid': {'read_only': True},
            'created_at': {'read_only': True},
        }
