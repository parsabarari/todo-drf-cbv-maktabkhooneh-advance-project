from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import (RegistrationSerializer,CustomTokenObtainPairSerializer,
                        # ChangePasswordSerializer, ProfileSerializer
                        )
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.views import TokenObtainPairView

class RegistrationApiView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'email':serializer.validated_data['email']
            }
            return Response(data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer