from rest_framework.generics import ListAPIView

from apps.news.models import MovieNews
from .serializer import MovieNewsListSerializer


class MovieNewsListView(ListAPIView):
    queryset = MovieNews.objects.all()
    serializer_class = MovieNewsListSerializer

    def get_queryset(self):
        return self.queryset.filter(is_active=True)
    