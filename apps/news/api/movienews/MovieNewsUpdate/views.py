from rest_framework.generics import UpdateAPIView

from apps.news.models import MovieNews
from .serializer import MovieNewsUpdateSerializer


class MovieNewsUpdateView(UpdateAPIView):
    queryset = MovieNews.objects.all()
    serializer_class = MovieNewsUpdateSerializer
    lookup_field = 'slug'
    
    def get_queryset(self):
        return MovieNews.objects.filter(is_active=True).select_related("category", "country").prefetch_related("tags", "actor", "regisseurs", "ganres")
    