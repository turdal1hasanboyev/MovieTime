from rest_framework.generics import CreateAPIView

from apps.common.permissions import IsAdminUserOrReadOnly
from apps.movie.models import AdditionalInfo
from .serializers import AdditionalInfoCreateSerializer


class AdditionalInfoCreateView(CreateAPIView):
    """
    Create additional info for movie
    """
    
    permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = AdditionalInfoCreateSerializer
    queryset = AdditionalInfo.objects.all()

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related("movie")
    