from rest_framework.generics import CreateAPIView

from apps.news.models import MovieNews
from .serializer import MovieNewsCreateSerializer


class MovieNewsCreateView(CreateAPIView):
    queryset = MovieNews.objects.all()
    serializer_class = MovieNewsCreateSerializer
    