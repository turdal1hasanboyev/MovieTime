from rest_framework.serializers import ModelSerializer

from apps.movie.models import AdditionalInfo


class AdditionalInfoDeleteSerializer(ModelSerializer):
    class Meta:
        model = AdditionalInfo
        fields = ['uuid', "movie", "key", "value", "created_at"]
        