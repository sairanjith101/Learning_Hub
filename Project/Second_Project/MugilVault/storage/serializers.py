from rest_framework import serializers
from .models import File

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ["id", "filename", "size", "uploaded_at", "file"]
        read_only_fields = ["filename", "size", "uploaded_at"]