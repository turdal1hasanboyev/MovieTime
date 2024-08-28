from rest_framework.generics import CreateAPIView

from apps.movie.models import Review
from .serializer import ReviewCreateSerializer
from apps.common.permissions import IsAdminUserOrReadOnly


class ReviewCreateView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def get_queryset(self):
        return Review.objects.filter(is_active=True).select_related("movie", 'user')
    