from rest_framework.generics import ListAPIView

from apps.movie.models import Review
from .serializer import ReviewListSerializer


class ReviewListView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer

    def get_queryset(self):
        return Review.objects.filter(is_active=True).select_related("movie", 'user')
    