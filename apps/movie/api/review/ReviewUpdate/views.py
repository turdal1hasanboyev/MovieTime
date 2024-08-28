from rest_framework.generics import UpdateAPIView

from apps.movie.models import Review
from .serializer import ReviewUpdateSerializer
from apps.common.permissions import IsAdminUserOrReadOnly


class ReviewUpdateView(UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewUpdateSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    lookup_field = 'movie'

    def get_queryset(self):
        return Review.objects.filter(is_active=True).select_related("movie", 'user')
    