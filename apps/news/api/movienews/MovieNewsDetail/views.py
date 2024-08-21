from rest_framework.generics import RetrieveAPIView

from apps.news.models import MovieNews
from .serializer import MovieNewsRetrieveSerializer


class MovieNewsRetrieveView(RetrieveAPIView):
    queryset = MovieNews.objects.all()
    serializer_class = MovieNewsRetrieveSerializer
    lookup_field = "slug"

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related("category", "country").prefetch_related("tags", "actor", "regisseurs", "ganres")
    