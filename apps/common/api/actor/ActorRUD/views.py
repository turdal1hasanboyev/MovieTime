from rest_framework.generics import RetrieveUpdateDestroyAPIView

from apps.common.models import Actor
from .serializer import ActorRUDSerializer


class ActorRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.filter(is_active=True)
    serializer_class = ActorRUDSerializer
    lookup_field = 'name'
    
    def perform_destroy(self, instance):
        instance.is_active = False
        
        instance.save()
        