"""
URL configuration for mugilvault project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

# Simple homepage view
def home(request):
    html = """
    <html>
        <head>
            <title>Welcome to MugilVault</title>
        </head>
        <body>
            <h1>Welcome to MugilVault!</h1>
            <ul>
                <li><a href="/swagger/" target="_blank">Swagger UI</a></li>
                <li><a href="/redoc/" target="_blank">Redoc</a></li>
                <li><a href="https://github.com/sairanjith101/Learning_Hub/tree/f7488044de87db9cf58a9b5ff33d06c6c316fd96/Project/Second_Project" targ>
            </ul>
        </body>
    </html>
    """
    return HttpResponse(html)

schema_view = get_schema_view(
    openapi.Info(
        title="MugilVault API",
        default_version="v1",
        description="Cloud Storage System APIs",
        contact=openapi.Contact(email="mugilvault@cloud.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path("api/auth/", include("users.urls")),
    path("api/", include("storage.urls")),

    # Swagger UI
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

# Media files serve panna (local only)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
