from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework.authtoken.models import Token
from authentication.send_mail import send_message_to_email
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(min_length=5, write_only=True)
    password2 = serializers.CharField(min_length=5, write_only=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def validate(self, attrs):
        password1 = attrs.get("password1")
        password2 = attrs.pop("password2")
        if password1 != password2:
            raise serializers.ValidationError(f"Пароли не совпадают")
        return attrs

    def create(self, validate_data):
        password = validate_data.pop("password1")
        user = User.objects.create_user(**validate_data, password=password)
        user.is_active = False
        user.save()
        send_message_to_email(user.email, user.activation_code)
        return user


class LoginJWTSerializer(TokenObtainPairSerializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(max_length=100, write_only=True)

    def validate(self, attrs):
        user = authenticate(email=attrs.pop("email"), password=attrs.pop("password"))
        if not user:
            raise serializers.ValidationError({
                "error": "such user does not exist"
            })
        if user and user.is_active:
            refresh = self.get_token(user)
            attrs["refresh"] = str(refresh)
            attrs["access"] = str(refresh.access_token)

        return attrs


class PasswordChangeSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, required=True, write_only=True)
    new_password = serializers.CharField(max_length=255, required=True, write_only=True)
    confirm_new_password = serializers.CharField(max_length=255, required=True, write_only=True)

    class Meta:
        model = User
        fields = ("password", "new_password", "confirm_new_password")

    def validate(self, attrs):
        if attrs["new_password"] != attrs["confirm_new_password"]:
            raise serializers.ValidationError({"error": "Password fields did not match"})
        return attrs

    def validate_old_password(self, value):
        user = self.context["request"].user
        if not user.check_password(value):
            raise serializers.ValidationError({"error": "Old password is not correct"})

    def update(self, instance, validated_data):
        instance.set_password(validated_data["new_password"])
        instance.save()
        return instance
