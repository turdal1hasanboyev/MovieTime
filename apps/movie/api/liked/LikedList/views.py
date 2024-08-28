from rest_framework.generics import ListAPIView

from apps.movie.models import Liked
from .serializer import LikedListSerializer


class LikedListView(ListAPIView):
    queryset = Liked.objects.all()
    serializer_class = LikedListSerializer
    pagination_class = None

    def get_queryset(self):
        return Liked.objects.filter(is_active=True).select_related("movie", 'user')
    