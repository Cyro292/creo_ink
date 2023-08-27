from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ["id", "email", "password", "birthday", "first_name", "last_name"]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = self.Meta.model(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(email=email, password=password)
        if not user:
            raise serializers.ValidationError("Invalid credentials")

        attrs["user"] = user
        return attrs


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "username", "email", "first_name", "last_name", "password"]
        read_only_fields = ["id"]  # Mark the 'id' field as read-only
        write_only_fields = ["password"]

    def update(self, instance, validated_data):
        # Allow updating user data
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.save()

        password = validated_data.get("password")
        if password:
            instance.set_password(password)

        instance.save()
        return instance

    def validate(self, attrs):
        # Custom password validation if required
        password = attrs.get("password")
        if password and len(password) < 8:
            raise serializers.ValidationError(
                "Password should be at least 8 characters long."
            )

        return attrs


class UserSettingsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["settings"]

    def validate(self, attrs):
        return super().validate(attrs)
