"""anpr URL Configuration

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
from app import views 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('logs/', views.logs, name="logs"),
    path('stats/', views.stats, name="stats"),
    # path('addcars/', views.car_upload, name="car_upload"),
    path('logout/', views.logoutUser, name="logout"),
    path('profile/', views.updateProfile, name="profile"),
    path('update_profile/', views.updateProfile, name="update_profile"),
    path('getlocation/', views.get_location, name="get_location"),
    path('uploadvideo/', views.uploadvideo, name="uploadvideo"),
    path('videolist/', views.videolist, name="videolist"),
    path('savevideo/<int:timestamp>/<str:type>/', views.intermediate, name="savevid"),
    path('remote/', views.remote, name="remote"),
    path('dashboard/<str:name>/', views.video_detection, name="video_detection"),
    path('alerts/', views.wapalert, name="wapalert"),
    path('addusers/', views.addusers, name="addusers"),
    path('video_feed/<int:timestamp>/', views.video_feed, name="video_feed"),
    path('webcam_feed/<int:timestamp>/', views.webcam_feed, name="webcam_feed"),
    path('live/', views.live, name="live"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
