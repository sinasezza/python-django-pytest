from django.urls import path
from . import apis


app_name = "fibonacci_api"

urlpatterns = [
    path("", apis.calc_fibonacci, name="calc_fibonacci"),
]
