from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='show-events'),
    path('<int:pk>', views.detail, name='event-detail') 
]