from rest_framework.generics import RetrieveAPIView

from apps.movie.models import MovieImage
from .serializer import MovieImageRetrieveSerializer


class MovieImageRetrieveView(RetrieveAPIView):
    queryset = MovieImage.objects.all()
    serializer_class = MovieImageRetrieveSerializer
    lookup_field = 'movie'

    def get_queryset(self):
        return MovieImage.objects.filter(is_active=True).select_related("movie")
    