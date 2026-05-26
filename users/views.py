from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters

from .filters import PaymentFilter
from .models import CustomUser,Payment
from .serializers import UserProfileSerializer, PaymentSerializer


class UserProfileAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    queryset = CustomUser.objects.all()


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = PaymentFilter
    ordering_fields = ['payment_date']
    ordering = ['-payment_date'] # по умолчанию сначала новые
