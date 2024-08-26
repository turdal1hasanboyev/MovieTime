from rest_framework.generics import ListAPIView

from apps.movie.models import Movie
from .serializer import MovieListSerializer


class MovieListView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related('category', 'country').prefetch_related('genres', 'awards', 'actors', 'regisseurs')
