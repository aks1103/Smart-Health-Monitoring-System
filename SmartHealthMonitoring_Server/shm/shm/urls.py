"""shm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from shmApp.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    

    url(r'^pedo/', pedo),
    url(r'^pedodata/', pedodata),

    url(r'^1/', hello),
    url(r'^2/', hello2),
    url(r'^3/', hello3),
    url(r'^4/', hello4),
    url(r'^5/', hello5),

    url(r'^pushup/', pushup),
    url(r'^pushupdata/', pushupdata),

    # Sleep Data from heart rate sensor
    url(r'^sleep/', sleep),
    url(r'^sleepdata/', sleepdata),

    url(r'^ldr/', ldr),
    url(r'^ldrdata/', ldrdata),


    url(r'^chair/', chair),
    url(r'^chairdata/', chairdata),

    url(r'^sleepposture/', admin.site.urls),
    

    url(r'^time/', time),
    url(r'^t/', t),




]
