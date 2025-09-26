import os
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, status
from .models import File
from .serializers import FileSerializer
from .permissions import IsOwner
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from django.conf import settings
from django.core.files.storage import default_storage


import boto3
from botocore.exceptions import BotoCoreError, ClientError

class FileViewSet(viewsets.ModelViewSet):
    
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        
        user = self.request.user
        return File.objects.filter(owner=user).order_by("-uploaded_at")

    def perform_create(self, serializer):
        uploaded_file = self.request.FILES.get("file")
        if not uploaded_file:
            from rest_framework.exceptions import ValidationError
            raise ValidationError("No file provided")

        user = self.request.user
        used_space = File.objects.filter(owner=user).aggregate(total=Sum("size"))["total"] or 0
        quota = getattr(user, "storage_quota", None)

        if quota is not None and used_space + uploaded_file.size > quota:
            from rest_framework.exceptions import ValidationError
            raise ValidationError("Storage quota exceeded. Delete files or upgrade plan.")

        # Let Django handle S3 upload automatically
        serializer.save(
            owner=user,
            filename=uploaded_file.name,
            size=uploaded_file.size,
            file=uploaded_file
        )

    def perform_update(self, serializer):
        instance = self.get_object()
        uploaded_file = self.request.FILES.get("file")
        new_filename = self.request.data.get("filename")

        # Case 1: New file uploaded (replace existing)
        if uploaded_file:
            # Delete old file from S3
            if instance.file:
                instance.file.delete(save=False)
            # Django storage automatically handles S3 upload & delete old file
            serializer.save(
                file=uploaded_file,
                filename=uploaded_file.name,
                size=uploaded_file.size
            )
            return

        # Case 2: Rename only
        if new_filename and new_filename != instance.filename:
            old_name = instance.file.name
            ext = os.path.splitext(old_name)[1]
            base_name = os.path.splitext(new_filename)[0]
            new_name_with_ext = f"{base_name}{ext}"
            new_path = os.path.join("uploads", new_name_with_ext)

            # Use default_storage to rename
            from django.core.files.storage import default_storage

            # Copy file to new path
            with default_storage.open(old_name, "rb") as f:
                default_storage.save(new_path, f)
            
            # Delete old file
            default_storage.delete(old_name)

            # Update instance
            instance.file.name = new_path
            instance.filename = new_name_with_ext
            instance.save(update_fields=["file", "filename"])
            return

        serializer.save()



    @action(detail=False, methods=["get"], url_path="usage")
    def usage(self, request):
        
        user = request.user
        used_space = File.objects.filter(owner=user).aggregate(total=Sum("size"))["total"] or 0
        quota = getattr(user, "storage_quota", None)

        if quota is None:
            return Response({
                "used_space": used_space,
                "storage_quota": None,
                "remaining_space": None,
                "detail": "No quota set for this user."
            })

        remaining_space = quota - used_space
        return Response({
            "used_space": used_space,
            "remaining_space": max(remaining_space, 0),
            "storage_quota": quota,
        })


    @action(detail=True, methods=["get"], url_path="share")
    def share(self, request, pk=None):
        
        file_obj = get_object_or_404(File, pk=pk, owner=request.user)

        if getattr(settings, "AWS_STORAGE_BUCKET_NAME", ""):
            try:
                s3 = boto3.client(
                    "s3",
                    aws_access_key_id=getattr(settings, "AWS_ACCESS_KEY_ID", None),
                    aws_secret_access_key=getattr(settings, "AWS_SECRET_ACCESS_KEY", None),
                    region_name=getattr(settings, "AWS_REGION", None),
                )
                url = s3.generate_presigned_url(
                    "get_object",
                    Params={"Bucket": settings.AWS_STORAGE_BUCKET_NAME, "Key": file_obj.file.name},
                    ExpiresIn=300,  # 5 minutes
                )
                return Response({"shareable_link": url})
            except (BotoCoreError, ClientError) as e:
                return Response({"detail": "Failed to generate S3 URL", "error": str(e)},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        link = request.build_absolute_uri(file_obj.file.url)
        return Response({"link": link})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.file.delete(save=False)  # deletes from S3 automatically
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
