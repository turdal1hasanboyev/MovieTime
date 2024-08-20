from rest_framework.generics import DestroyAPIView

from apps.common.models import Category
from .serializer import CategoryDestroySerializer


class CategoryDestroyView(DestroyAPIView):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategoryDestroySerializer
    lookup_field = "name"

    def perform_destroy(self, instance):
        instance.is_active = False
        
        instance.save()
