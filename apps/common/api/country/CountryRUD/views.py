from rest_framework.generics import RetrieveUpdateDestroyAPIView

from apps.common.models import Country
from .serializer import CountryRUDSerializer


class CountryRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.filter(is_active=True)
    serializer_class = CountryRUDSerializer
    lookup_field = 'name'
    
    def perform_destroy(self, instance):
        instance.is_active = False
        
        instance.save()
        