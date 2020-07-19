from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('skill/<slug>', views.SkillDetailPage.as_view(),name='skill-detail'),
    path('works/', views.Works.as_view(), name='works'),
    path('me/', views.Me, name='me')
]
