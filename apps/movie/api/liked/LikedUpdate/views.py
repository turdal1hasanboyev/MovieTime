from rest_framework.generics import UpdateAPIView

from apps.movie.models import Liked
from .serializer import LikedUpdateSerializer
from apps.common.permissions import IsAdminUserOrReadOnly


class LikedUpdateView(UpdateAPIView):
    queryset = Liked.objects.all()
    serializer_class = LikedUpdateSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    lookup_field = 'movie'

    def get_queryset(self):
        return Liked.objects.filter(is_active=True).select_related("movie", 'user')
    