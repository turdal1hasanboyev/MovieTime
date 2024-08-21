from rest_framework.generics import CreateAPIView

from apps.news.models import MovieNews
from .serializer import MovieNewsCreateSerializer


class MovieNewsCreateView(CreateAPIView):
    queryset = MovieNews.objects.all()
    serializer_class = MovieNewsCreateSerializer

    def get_queryset(self):
        return self.queryset.all().select_related("category", "country").prefetch_related("tags", "actor", "regisseurs", "ganres")
    