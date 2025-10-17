from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()

    def validate_age(self, value):
        if value < 18:
            raise serializers.ValidationError("Age must be at least 18")
        return value

class EvenvSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    start_date = serializers.DateField()
    end_date = serializers.DateField()

    def validate_date(self, data):
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError("End date must be grater than start date")
        return data