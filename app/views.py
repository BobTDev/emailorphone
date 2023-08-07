from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Register

from .serializers import UserSerializer

User = get_user_model()

# Create your views here.

import re
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = Register.objects.filter().first()
        refresh_token = RefreshToken.for_user(user)

        email_or_phone = serializer.validated_data['email_or_phone']
        if re.match(re.compile(r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'), email_or_phone):
            return Response({
                'message': "User is registering with email",
                'refresh': str(refresh_token),
                'access': str(refresh_token.access_token)
            }, status=status.HTTP_201_CREATED)
        elif re.match(re.compile(r'^[+]?[(]?[0-9]{3}[)]?[-\s\]?[0-9]{3}[-\s\]?[0-9]{4,6}$'), email_or_phone):
            return Response({
                "message": "User is registering with phone number",
                'refresh': str(refresh_token),
                'access': str(refresh_token.access_token)
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "message": "Invalid email or phone number"
            }, status=status.HTTP_400_BAD_REQUEST)
