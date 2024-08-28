from rest_framework.generics import ListAPIView

from apps.movie.models import AdditionalInfo
from .serializers import AdditionalInfoListSerializer


class AdditionalInfoListView(ListAPIView):
    queryset = AdditionalInfo.objects.all()
    serializer_class = AdditionalInfoListSerializer

    def get_queryset(self):
        return AdditionalInfo.objects.filter(is_active=True).select_related("movie")
    