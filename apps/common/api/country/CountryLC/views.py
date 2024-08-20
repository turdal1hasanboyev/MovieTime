from rest_framework.generics import ListCreateAPIView

from apps.common.models import Country
from .serializer import CountryLCSerializer


class CountryLCView(ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryLCSerializer

    def get_queryset(self):
        return self.queryset.filter(is_active=True)
    