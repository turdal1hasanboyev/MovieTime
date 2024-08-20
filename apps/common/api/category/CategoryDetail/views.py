from rest_framework.generics import RetrieveAPIView

from apps.common.models import Category
from .serializer import CategoryRetrieveSerializer


class CategoryRetrieveView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryRetrieveSerializer
    lookup_field = "name"

    def get_queryset(self):
        return self.queryset.filter(is_active=True)
    