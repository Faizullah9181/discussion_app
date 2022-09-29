from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User as AuthUser
from .models import Users
from django.contrib.auth.hashers import make_password
from rest_framework import status


class UserSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(default=True)

    class Meta:
        model = Users
        fields = '__all__'




class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Users
        fields = '__all__'

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)