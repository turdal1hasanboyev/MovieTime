from rest_framework.generics import DestroyAPIView

from apps.movie.models import AdditionalInfo
from .serializers import AdditionalInfoDeleteSerializer


class AdditionalInfoDestroyView(DestroyAPIView):
    """
    Destroy a model instance.
    """
    queryset = AdditionalInfo.objects.all()
    serializer_class = AdditionalInfoDeleteSerializer
    lookup_field = "movie"

    def get_queryset(self):
        return AdditionalInfo.objects.filter(is_active=True).select_related("movie")
    
    def perform_destroy(self, instance):
        instance.is_active = False
        
        instance.save() 
    