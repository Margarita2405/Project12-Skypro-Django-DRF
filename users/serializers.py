from rest_framework import serializers

from users.models import CustomUser, Payment


class PaymentBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'payment_date', 'amount', 'payment_method', 'course', 'lesson']


class UserProfileSerializer(serializers.ModelSerializer):
    payments = PaymentBriefSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'phone', 'city', 'avatar', 'payments']
        read_only_fields = ['email'] # чтобы email нельзя было изменить через профиль


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
