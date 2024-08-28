from rest_framework.generics import DestroyAPIView

from apps.movie.models import Review
from .serializer import ReviewDestroySerializer


class ReviewDestroyView(DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewDestroySerializer
    lookup_field = 'movie'

    def get_queryset(self):
        return Review.objects.filter(is_active=True).select_related("movie", 'user')
    
    def perform_destroy(self, instance):
        instance.is_active = False
        
        instance.save() 
