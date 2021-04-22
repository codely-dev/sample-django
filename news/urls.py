from django.urls import path
from . import views
from .views import ArticleList

urlpatterns = [
    path('', ArticleList.as_view(), name='show-articles'),
]