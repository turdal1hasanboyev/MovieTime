from rest_framework.generics import UpdateAPIView

from apps.common.permissions import IsAdminUserOrReadOnly
from apps.movie.models import AdditionalInfo
from .serializers import AdditionalInfoUpdateSerializer


class AdditionalInfoUpdateView(UpdateAPIView):
    """
    Update additional info for movie
    """
    
    permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = AdditionalInfoUpdateSerializer
    queryset = AdditionalInfo.objects.all()
    lookup_field = 'movie'

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related("movie")
    