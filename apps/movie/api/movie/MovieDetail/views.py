from rest_framework.generics import RetrieveAPIView

from apps.movie.models import Movie
from .serializer import MovieDetailSerializer


class MovieDetailView(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer
    lookup_field = "slug"

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related('category', 'country').prefetch_related('genres', 'awards', 'actors', 'regisseurs')
