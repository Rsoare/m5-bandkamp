from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="A user with that username already exists.",
            )
        ]
    )
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = [
            "id",
            "full_name",
            "artistic_name",
            "password",
            "username",
            "email",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        new_password = validated_data.get('password')
        if new_password:
            instance.password = make_password(new_password)

        instance.save()

        return instance
