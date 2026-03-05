from rest_framework import serializers
from .base import BaseSerializer
from db.models import User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "role",
            "user_timezone",
            "cover_image"
        ]
