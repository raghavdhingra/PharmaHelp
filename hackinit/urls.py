"""hackinit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import main.views as mainView
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from hackinit.settings import *
from main.serializer import *

urlpatterns = [
    path('admin', admin.site.urls),
    path('', mainView.home,name="home"),
    path('find-labs', mainView.lab,name="lab"),
    path('find-pharmacies', mainView.pharmacy,name="pharmacy"),
    path('recommendations', mainView.recommend,name="recommend"),
    path('send-mail', mainView.sendMail,name="sendmail"),
    path('labapi', mainView.LabList.as_view()),
]
