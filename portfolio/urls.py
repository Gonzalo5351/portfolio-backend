"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.http import JsonResponse
from django.conf import settings
from django.http import HttpResponse
import os

from mimetypes import guess_type
from django.http import FileResponse, Http404

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),  # Initial page
    path("projects/<int:project_id>/", views.project_detail, name="project_detail"),
    path("contact/", views.contact, name="contact"),
    path("auth/", include("portfolio.urls_auth")),  # Authentication URL
    path("manage-projects/", views.manage_projects, name="manage_projects"),
    path("add-project/", views.add_project, name="add_project"),
]


def staticfiles_debug_view(request):
    # Ruta del directorio donde se recopilan los archivos estáticos
    staticfiles_dir = settings.STATIC_ROOT
    if os.path.exists(staticfiles_dir):
        files = []
        for root, dirs, filenames in os.walk(staticfiles_dir):
            for filename in filenames:
                relative_path = os.path.relpath(
                    os.path.join(root, filename), staticfiles_dir
                )
                files.append(relative_path)
        return JsonResponse({"files": files})
    return JsonResponse({"error": "No static files found."}, status=404)


urlpatterns += [
    path("staticfiles-debug/", staticfiles_debug_view),
]


def debug_static_file(request, file_path):
    file_full_path = os.path.join(settings.STATIC_ROOT, file_path)
    if not os.path.exists(file_full_path):
        return HttpResponse("File not found.", status=404)

    # Detectar el tipo MIME del archivo
    mime_type, _ = guess_type(file_full_path)
    try:
        return FileResponse(open(file_full_path, "rb"), content_type=mime_type)
    except Exception:
        raise Http404("Unable to read the file.")


urlpatterns += [
    path("debug-static/<str:file_path>/", debug_static_file),
]
