from django.urls import path
from . import views
from .models import Link as lilink

urlpatterns = [
    path('', views.get_link, name="link"),
]
