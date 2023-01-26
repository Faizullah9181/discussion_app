from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
Users = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(default=True)

    class Meta:
        model = Users
        fields = '__all__'




class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    fcm_token = serializers.CharField(required=False)

    class Meta:
        model = Users
        fields = '__all__'

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)

    def create(self, validated_data):
        user = super().create(validated_data)
        fcm_token = validated_data.get('fcm_token', None)
        if fcm_token:
            user.fcm_token = fcm_token
            user.save()
        return user
