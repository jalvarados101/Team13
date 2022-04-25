"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
# from re import template
from django.contrib import admin
from django.urls import include , path
# from django.views.generic.base import TemplateView
from rest_framework import routers
from songrater import views

router = routers.DefaultRouter()

router.register(r'songraters', views.SongRaterView, 'songrater')
router.register(r'ratings', views.RatingsView, 'rating')
router.register(r'users', views.UserView, 'user')
router.register(r'songs', views.SongView, 'song')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('', include('songrater.urls')),
    # path('songrater/', include('songrater.urls')),
    # path('songrater/', include('django.contrib.auth.urls')),
    # path('', TemplateView.as_view(template_name = 'home.html'), name='home'),
]