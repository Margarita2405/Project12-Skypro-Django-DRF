from rest_framework import generics
from .models import CustomUser
from .serializers import UserProfileSerializer


class UserProfileAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    queryset = CustomUser.objects.all()
