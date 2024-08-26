from rest_framework.generics import DestroyAPIView

from apps.movie.models import Movie
from .serializer import MovieDestroySerializer


class MovieDeleteView(DestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDestroySerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Movie.objects.filter(is_active=True).select_related('category', 'country').prefetch_related('genres', 'awards', 'actors', 'regisseurs')
    
    def perform_destroy(self, instance):
        instance.is_active = False
        
        instance.save() 
