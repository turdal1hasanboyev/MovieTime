from rest_framework.generics import UpdateAPIView

from apps.movie.models import Movie
from .serializer import MovieUpdateSerializer
from apps.common.permissions import IsAdminUserOrReadOnly


class MovieUpdateView(UpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieUpdateSerializer
    lookup_field = 'slug'
    permission_classes = [IsAdminUserOrReadOnly]

    def get_queryset(self):
        return Movie.objects.filter(is_active=True).select_related('category', 'country').prefetch_related('genres', 'awards', 'actors', 'regisseurs')
