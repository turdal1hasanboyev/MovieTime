from rest_framework.generics import CreateAPIView

from apps.movie.models import MovieImage
from .serializer import MovieImageCreateSerializer
from apps.common.permissions import IsAdminUserOrReadOnly


class MovieImageCreateView(CreateAPIView):
    queryset = MovieImage.objects.all()
    serializer_class = MovieImageCreateSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def get_queryset(self):
        return MovieImage.objects.filter(is_active=True).select_related("movie")
    