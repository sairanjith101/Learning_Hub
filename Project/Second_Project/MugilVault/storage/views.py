from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import File
from .serializers import FileSerializer
from .permissions import IsOwner

import boto3
from django.conf import settings
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from storage import models
from django.db.models import Sum




class FileViewSet(viewsets.ModelViewSet):
    serializer_class = FileSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return File.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        uploaded_file = self.request.FILES["file"]
        user = self.request.user
        used_space = File.objects.filter(owner=user).aggregate(total=Sum("size"))["total"] or 0

        if used_space + uploaded_file.size > user.storage_quota:
            from rest_framework.exceptions import ValidationError
            raise ValidationError("Storage quota exceeded. Delete files or upgrade plan.")
        
        serializer.save(
            owner=self.request.user,
            filename=uploaded_file.name,
            size=uploaded_file.size,
        )

    # New action for quota usage [ GET http://127.0.0.1:8000/api/files/usage/ ]
    @action(detail=False, methods=["get"])
    def usage(self, request):
        user = request.user
        used_space = File.objects.filter(owner=user).aggregate(total=Sum("size"))["total"] or 0
        remaining_space = user.storage_quota - used_space
        return Response({
            "used_space": used_space,
            "remaining_space": max(remaining_space, 0),
            "storage_quota": user.storage_quota,
        })

    # Generate temporary share link
    @action(detail=True, methods=["get"])
    def share(self, request, pk=None):
        file_obj = self.get_object()
        if settings.AWS_STORAGE_BUCKET_NAME:  # AWS S3
            s3 = boto3.client(
                "s3",
                aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                region_name=settings.AWS_REGION,
            )
            url = s3.generate_presigned_url(
                "get_object",
                Params={"Bucket": settings.AWS_STORAGE_BUCKET_NAME, "Key": file_obj.file.name},
                ExpiresIn=300,  # 5 min expiry
            )
            return Response({"shareable_link": url})
        else:  # fallback local storage
            return Response({"link": request.build_absolute_uri(file_obj.file.url)})
