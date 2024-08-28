from rest_framework.generics import RetrieveAPIView

from apps.movie.models import Liked
from .serializer import LikedRetrieveSerializer


class LikedRetrieveView(RetrieveAPIView):
    queryset = Liked.objects.all()
    serializer_class = LikedRetrieveSerializer
    lookup_field = 'movie'

    def get_queryset(self):
        return Liked.objects.filter(is_active=True).select_related("movie", 'user')
    