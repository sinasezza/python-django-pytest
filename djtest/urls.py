"""
URL configuration for djtest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib.auth.views import LoginView
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", LoginView.as_view(template_name="admin/login.html")),
    path("companies/", include("companies.urls", namespace="companies")),
    path("api/fibonacci/", include("fibonacci.api.urls", namespace="fibonacci-api")),
]
