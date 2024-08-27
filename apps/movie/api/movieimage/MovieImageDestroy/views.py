from rest_framework.generics import DestroyAPIView

from apps.movie.models import MovieImage
from .serializer import MovieImageDestroySerializer


class MovieImageDestroyView(DestroyAPIView):
    queryset = MovieImage.objects.all()
    serializer_class = MovieImageDestroySerializer
    lookup_field = 'movie'

    def get_queryset(self):
        return MovieImage.objects.filter(is_active=True).select_related("movie")
    
    def perform_destroy(self, instance):
        instance.is_active = False
        
        instance.save() 
