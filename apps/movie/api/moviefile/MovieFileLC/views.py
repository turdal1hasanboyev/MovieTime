from rest_framework.generics import ListCreateAPIView

from apps.movie.models import MovieFile
from .serializers import MovieFileLCSerializer


class MovieFileLCView(ListCreateAPIView):
    """
    List and create movie files.
    """
    queryset = MovieFile.objects.all()
    serializer_class = MovieFileLCSerializer

    def get_queryset(self):
        return MovieFile.objects.filter(is_active=True).select_related("movie")
