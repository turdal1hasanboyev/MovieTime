from rest_framework.generics import DestroyAPIView

from apps.movie.models import Liked
from .serializer import LikedDestroySerializer


class LikedDestroyView(DestroyAPIView):
    queryset = Liked.objects.all()
    serializer_class = LikedDestroySerializer
    lookup_field = 'movie'

    def get_queryset(self):
        return Liked.objects.filter(is_active=True).select_related("movie", 'user')
    
    def perform_destroy(self, instance):
        instance.is_active = False
        
        instance.save() 
