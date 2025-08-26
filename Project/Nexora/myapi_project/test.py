from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, require=True)
    role = serializers.ChoiceField(choices=User.Roles.choices, default = User.Roles.CUSTOMER)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'address', 'phone', 'role')

    def validate_password(self, value):
        validate_password(value)
        return value
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'address', 'role')
        read_only_fields = ('id', 'username', 'email', 'role')