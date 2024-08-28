from rest_framework.serializers import ModelSerializer

from apps.movie.models import Liked
from apps.movie.api.movie.MovieDetail.serializer import MovieDetailSerializer
from apps.user.api.CustomUser.serializer import UserSerializer


class LikedListSerializer(ModelSerializer):
    movie = MovieDetailSerializer
    user = UserSerializer

    class Meta:
        model = Liked
        fields = [
            'uuid',
            'movie',
            'user',
            'like',
            'created_at',
        ]
