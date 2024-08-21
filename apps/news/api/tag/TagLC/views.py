from rest_framework.generics import ListCreateAPIView

from apps.news.models import Tag
from .serializer import TagLCSerializer


class TagLCView(ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagLCSerializer

    def get_queryset(self):
        return self.queryset.filter(is_active=True)
    