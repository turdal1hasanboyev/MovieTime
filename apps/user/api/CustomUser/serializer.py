from apps.user.models import User
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "avatar",
            "last_name",
            "email",
            "phone_number",
        )
