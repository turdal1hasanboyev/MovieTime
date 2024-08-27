from rest_framework.generics import UpdateAPIView

from apps.movie.models import MovieImage
from .serializer import MovieImageUpdateSerializer
from apps.common.permissions import IsAdminUserOrReadOnly


class MovieImageUpdateView(UpdateAPIView):
    queryset = MovieImage.objects.all()
    serializer_class = MovieImageUpdateSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    lookup_field = 'movie'

    def get_queryset(self):
        return MovieImage.objects.filter(is_active=True).select_related("movie")
    