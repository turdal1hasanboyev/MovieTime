from rest_framework.generics import RetrieveAPIView

from apps.movie.models import Review
from .serializer import ReviewRetrieveSerializer


class ReviewRetrieveView(RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewRetrieveSerializer
    lookup_field = 'movie'

    def get_queryset(self):
        return Review.objects.filter(is_active=True).select_related("movie", 'user')
    