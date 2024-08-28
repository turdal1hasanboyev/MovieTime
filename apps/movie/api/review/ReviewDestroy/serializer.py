from rest_framework.serializers import ModelSerializer

from apps.movie.models import Review


class ReviewDestroySerializer(ModelSerializer):
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
        