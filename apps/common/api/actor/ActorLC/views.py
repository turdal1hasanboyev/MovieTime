from rest_framework.generics import ListCreateAPIView

from apps.common.models import Actor
from .serializer import ActorLCSerializer
from apps.common.permissions import IsAdminUserOrReadOnly


class ActorLCView(ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorLCSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def get_queryset(self):
        return self.queryset.filter(is_active=True)
    