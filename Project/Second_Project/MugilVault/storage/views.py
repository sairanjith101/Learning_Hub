# storage/views.py
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, status
from .models import File
from .serializers import FileSerializer
from .permissions import IsOwner
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from django.conf import settings

# optional S3 support
import boto3
from botocore.exceptions import BotoCoreError, ClientError

class FileViewSet(viewsets.ModelViewSet):
    """
    CRUD for File model.
    - create: checks user's storage quota (if user has `storage_quota` attribute)
              saves filename and size automatically.
    - retrieve/list: owner-only (by default) unless you change permissions.
    - share (action): returns a pre-signed S3 URL if S3 is configured,
                      otherwise a direct local URL.
    """
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        # users should see only their own files
        user = self.request.user
        return File.objects.filter(owner=user).order_by("-uploaded_at")

    def perform_create(self, serializer):
        """
        Called on POST to create. Populate filename and size.
        Enforce storage quota if available on user model.
        """
        uploaded_file = self.request.FILES.get("file")
        if uploaded_file is None:
            return Response({"detail": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)

        user = self.request.user

        # check used space (sum of sizes) — if no files, sum is None -> 0
        used_space = File.objects.filter(owner=user).aggregate(total=Sum("size"))["total"] or 0

        # user.storage_quota expected to be integer bytes; fallback to None (no quota)
        quota = getattr(user, "storage_quota", None)

        if quota is not None:
            if used_space + uploaded_file.size > quota:
                from rest_framework.exceptions import ValidationError
                raise ValidationError("Storage quota exceeded. Delete files or upgrade plan.")

        # Save filename and size manually (serializer has them read_only)
        serializer.save(
            owner=user,
            filename=uploaded_file.name,
            size=uploaded_file.size,
        )

    @action(detail=False, methods=["get"], url_path="usage")
    def usage(self, request):
        """
        Return how much storage the user has used and remaining.
        """
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
        """
        Return a shareable link for a file.
        If AWS_BUCKET configured, create a presigned S3 URL.
        Otherwise, return absolute URL for local media.
        """
        file_obj = get_object_or_404(File, pk=pk, owner=request.user)

        # If using AWS
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
        # fallback to local media
        link = request.build_absolute_uri(file_obj.file.url)
        return Response({"link": link})

    def destroy(self, request, *args, **kwargs):
        """
        Ensure file is deleted from storage if necessary (optional),
        but default Django FileField delete is OK for local storage.
        For S3 you may want to delete the object as well.
        """
        instance = self.get_object()
        # If S3, try to delete remote object too (optional)
        if getattr(settings, "AWS_STORAGE_BUCKET_NAME", ""):
            try:
                s3 = boto3.client(
                    "s3",
                    aws_access_key_id=getattr(settings, "AWS_ACCESS_KEY_ID", None),
                    aws_secret_access_key=getattr(settings, "AWS_SECRET_ACCESS_KEY", None),
                    region_name=getattr(settings, "AWS_REGION", None),
                )
                s3.delete_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=instance.file.name)
            except Exception:
                # ignore deletion error and continue to delete DB record/local file
                pass

        # delete DB record (and local file if configured)
        instance.file.delete(save=False)  # remove file
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
