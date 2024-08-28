from rest_framework.generics import RetrieveAPIView

from apps.movie.models import AdditionalInfo
from .serializers import AdditionalInfoDetailSerializer


class AdditionalInfoDetailView(RetrieveAPIView):
    queryset = AdditionalInfo.objects.all()
    serializer_class = AdditionalInfoDetailSerializer
    lookup_field = "movie"

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related("movie")
    