from rest_framework.serializers import ModelSerializer

from apps.movie.models import Review
from apps.movie.api.movie.MovieDetail.serializer import MovieDetailSerializer
from apps.user.api.CustomUser.serializer import UserSerializer


class ReviewRetrieveSerializer(ModelSerializer):
    movie = MovieDetailSerializer
    user = UserSerializer

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
