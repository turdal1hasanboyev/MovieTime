from rest_framework.generics import DestroyAPIView

from apps.news.models import MovieNews
from .serializer import MovieNewsDestroySerializer


class MovieNewsDestroyView(DestroyAPIView):
    queryset = MovieNews.objects.all()
    serializer_class = MovieNewsDestroySerializer
    lookup_field = "slug"

    def get_queryset(self):
        return MovieNews.objects.filter(is_active=True).select_related("category", "country").prefetch_related("tags", "actor", "regisseurs", "ganres")
    
    def perform_destroy(self, instance):
        instance.is_active = False
        
        instance.save()
