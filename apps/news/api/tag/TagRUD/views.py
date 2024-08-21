from rest_framework.generics import RetrieveUpdateDestroyAPIView

from apps.news.models import Tag
from .serializer import TagRUDSerializer


class TagRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.filter(is_active=True)
    serializer_class = TagRUDSerializer
    lookup_field = 'name'
    
    def perform_destroy(self, instance):
        instance.is_active = False
        
        instance.save()
        