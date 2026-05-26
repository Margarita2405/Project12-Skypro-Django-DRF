from django.urls import path

from .apps import UsersConfig
from .views import UserProfileAPIView, PaymentListAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('profile/<int:pk>/', UserProfileAPIView.as_view(), name='user_profile'),
    path('payments/', PaymentListAPIView.as_view(), name='payment_list'),
]
