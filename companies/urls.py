from django.urls import path
from rest_framework import routers
from . import views

app_name = "companies"

companies_router = routers.DefaultRouter()
companies_router.register("", viewset=views.CompanyViewSet, basename="companies")

urlpatterns = []

urlpatterns += companies_router.urls
