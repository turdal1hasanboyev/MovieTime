from rest_framework.generics import RetrieveUpdateDestroyAPIView

from apps.common.models import Award
from .serializer import AwardRUDSerializer


class AwardRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Award.objects.filter(is_active=True)
    serializer_class = AwardRUDSerializer
    lookup_field = 'name'
    
    def perform_destroy(self, instance):
        instance.is_active = False
        
        instance.save()
        