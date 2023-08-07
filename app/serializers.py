from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.response import Response

from .models import Register

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ['email_or_phone', 'full_name', 'password', 'username']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance



