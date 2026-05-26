from rest_framework import serializers

from users.models import CustomUser


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'phone', 'city', 'avatar']
        read_only_fields = ['email']  # чтобы email нельзя было изменить через профиль
