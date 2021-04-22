from django.urls import path
from . import views

urlpatterns = [
    path('', views.detail, name='profile-detail'),
]