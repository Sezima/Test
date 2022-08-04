from django.contrib.auth import authenticate

from rest_framework import serializers

from account.utils import send_activation_code
from main.models import Teacher


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, write_only=True)
    password_confirm = serializers.CharField(min_length=6, write_only=True)

    class Meta:
        model = Teacher
        fields = ('username', 'grade', 'phone_number', 'password', 'password_confirm')

    def validate(self, validated_data):
        password = validated_data.get('password')
        password_confirm = validated_data.get('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError('Password not right')
        return validated_data

    def create(self, validated_data):
        phone_number = validated_data.get('phone_number')
        password = validated_data.get('password')
        grade = validated_data.get('grade')
        username = validated_data.get('username')
        user = Teacher.objects.create_user(phone_number=phone_number, password=password, grade=grade, username=username)
        send_activation_code(phone_number=user.phone_number, activation_code=user.activation_code)

        return user


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=16)
    password = serializers.CharField(
        label='Password',
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        phone_number = attrs.get('phone_number')
        password = attrs.get('password')

        if phone_number and password:
            user = authenticate(request=self.context.get('request'), phone_number=phone_number, password=password)
            if not user:
                message = 'Unable to login'
                raise serializers.ValidationError(message, code='authorization')
        else:
            message = 'Must include "number" and "password".'
            raise serializers.ValidationError(message, code='authorization')

        attrs['user'] = user
        return attrs