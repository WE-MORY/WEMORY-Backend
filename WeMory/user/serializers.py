from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import update_last_login
from .models import User
from diary.serializers import UserDiarySerializer, GoalSerializer
from account.serializers import AccountSerializer

User = get_user_model()
JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER
JWT_ALLOW_REFRESH = api_settings.JWT_ALLOW_REFRESH
JWT_DECODE_HANDLER = api_settings.JWT_DECODE_HANDLER
JWT_PAYLOAD_GET_USER_ID_HANDLER = api_settings.JWT_PAYLOAD_GET_USER_ID_HANDLER

class SignUpSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    password_confirm = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            phone=validated_data['phone']
        )
        user.set_password(validated_data['password'])

        user.save()
        return user

class SignInSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=64)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=225, read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get('password', None)
        user = authenticate(email=email, password=password)

        if user is None:
            return {
                'email': 'None'
            }
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                '잘못된 이메일 또는 패스워드입니다.'
            )
        return {
            'email': user.email,
            'token': jwt_token
        }
        

class UserSerializer(serializers.ModelSerializer):
    diary_list = UserDiarySerializer(many=True, read_only=True)
    account = AccountSerializer(many=False, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'phone', 'diary_list', 'account')
