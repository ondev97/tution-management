"""tution_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import views



app_name='course'

urlpatterns = [
  path('create/',views.create_course,name = 'create'),
  path('',views.view_course,name = 'list'),
  path('delete/<int:pk>/',views.delete_course,name = 'delete'),
  path('module/<int:pk>/',views.single_course,name = 'single'),
  path('module/<str:cn>/',views.course_display,name = 'display'),

]

