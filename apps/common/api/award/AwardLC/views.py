from rest_framework.generics import ListCreateAPIView

from apps.common.models import Award
from .serializer import AwardLCSerializer


class AwardLCView(ListCreateAPIView):
    queryset = Award.objects.all()
    serializer_class = AwardLCSerializer

    def get_queryset(self):
        return self.queryset.filter(is_active=True)
    