from rest_framework.generics import ListAPIView

from apps.common.models import Country
from .serializer import CountryListSerializer


class CountryListView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryListSerializer

    def get_queryset(self):
        return self.queryset.filter(is_active=True)
    