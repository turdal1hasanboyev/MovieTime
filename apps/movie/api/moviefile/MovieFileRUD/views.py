from rest_framework.generics import RetrieveUpdateDestroyAPIView

from apps.movie.models import MovieFile
from .serializers import MovieFileRUDSerializer


class MovieFileRUDView(RetrieveUpdateDestroyAPIView):
    queryset = MovieFile.objects.all()
    serializer_class = MovieFileRUDSerializer
    lookup_field = 'movie'

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related("movie")
    
    def perform_destroy(self, instance):
        instance.is_active = False
        
        instance.save() 
