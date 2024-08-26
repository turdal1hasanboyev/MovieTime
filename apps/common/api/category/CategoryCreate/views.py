from rest_framework.generics import CreateAPIView

from apps.common.models import Category
from .serializer import CategoryCreateSerializer
from apps.common.permissions import IsAdminUserOrReadOnly


class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer
    permission_classes = {IsAdminUserOrReadOnly}
    