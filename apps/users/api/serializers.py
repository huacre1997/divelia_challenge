from django.contrib.auth import authenticate

from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        # Realiza la validación personalizada
        user = authenticate(username=email, password=password)
        if not user:
            raise serializers.ValidationError('Credenciales inválidas')

        data['user'] = user
        return data


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'department']
