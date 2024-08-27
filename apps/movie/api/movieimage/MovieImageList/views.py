from rest_framework.generics import ListAPIView

from apps.movie.models import MovieImage
from .serializer import MovieImageListSerializer


class MovieImageListView(ListAPIView):
    queryset = MovieImage.objects.all()
    serializer_class = MovieImageListSerializer
    pagination_class = None

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related("movie")
    