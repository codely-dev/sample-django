"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls import url
from django.views.generic import TemplateView
from .views import dashboard, homepage, Register

#Bilder
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('locations/', include('locations.urls')),
    path('events/', include('events.urls')),
    path('profile/', include('profiles.urls')),
    path('news/', include('news.urls')),
    path('dashboard/', dashboard),
    path('register/success/', TemplateView.as_view(template_name="registration/success.html"), name='register-success',),
    path('register/', Register.as_view(), name='register'),
    path('', include('django.contrib.auth.urls')),
    path('', include('pwa.urls')),
    #path('', include('pages.urls')),
    path('', homepage),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)