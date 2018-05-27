"""gyde URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import re_path
from django.contrib.auth import views as auth_views
from gyde1 import views

urlpatterns = [
    re_path(r'admin/', admin.site.urls),
    re_path(r'^signup/$', views.signup, name='signup'),
    re_path(r'^$', views.home, name='home'),
    # re_path(r'^login/$', views.login, name='login'),
    re_path(r'^login/$', auth_views.login, {'template_name': 'loginpage/login.html'}, name='login'),
    re_path(r'^profile/$', views.profile, name='profile'),

]
