from django.urls import path
from . import views
from .views import LocationList, LocationView

urlpatterns = [
    path('', LocationList.as_view(), name='show-locations'),
    path('<int:pk>', LocationView.as_view(), name='location-detail') 
]