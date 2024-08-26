from rest_framework.generics import CreateAPIView

from apps.movie.models import Movie
from .serializer import MovieCreateSerializer
from apps.common.permissions import IsAdminUserOrReadOnly


class MovieCreateView(CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieCreateSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def get_queryset(self):
        return Movie.objects.filter(is_active=True).select_related('category', 'country').prefetch_related('genres', 'awards', 'actors', 'regisseurs')
