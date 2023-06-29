from rest_framework import serializers
from .models import Album
from users.models import User


class UserResponse(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "artistic_name",
            "email",
            "full_name",
            "username",
        ]


class AlbumSerializer(serializers.ModelSerializer):
    user = UserResponse(read_only=True)

    class Meta:
        model = Album
        fields = [
            "id",
            "name",
            "year",
            "user",
        ]
