from rest_framework.generics import DestroyAPIView

from apps.news.models import MovieNews
from .serializer import MovieNewsDestroySerializer


class MovieNewsDestroyView(DestroyAPIView):
    queryset = MovieNews.objects.filter(is_active=True)
    serializer_class = MovieNewsDestroySerializer
    lookup_field = "slug"

    def perform_destroy(self, instance):
        instance.is_active = False
        
        instance.save()
