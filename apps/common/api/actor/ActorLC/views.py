from rest_framework.generics import ListCreateAPIView

from apps.common.models import Actor
from .serializer import ActorLCSerializer


class ActorLCView(ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorLCSerializer

    def get_queryset(self):
        return self.queryset.filter(is_active=True)
    