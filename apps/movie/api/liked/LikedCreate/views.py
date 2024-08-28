from rest_framework.generics import CreateAPIView

from apps.movie.models import Liked
from .serializer import LikedCreateSerializer
from apps.common.permissions import IsAdminUserOrReadOnly


class LikedCreateView(CreateAPIView):
    queryset = Liked.objects.all()
    serializer_class = LikedCreateSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def get_queryset(self):
        return Liked.objects.filter(is_active=True).select_related("movie", 'user')
    