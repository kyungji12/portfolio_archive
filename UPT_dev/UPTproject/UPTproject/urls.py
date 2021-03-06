"""UPTproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from pose_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name="home"),
    path('desc/', views.desc, name="desc"),
    path('workout/', views.workout, name="workout"),
    path('result/', views.result, name="result"),

    path('video_test/', views.video_test, name="video_test"),
    path('video_test2/', views.video_test2, name="video_test2"),
    path('video_test3/', views.video_test3, name="video_test3"),
]
