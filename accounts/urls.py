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
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


app_name='accounts'

urlpatterns = [
    path('',views.home,name="home"),
    path('register/',views.register,name="register"),
    path('sturegister/',views.studentregister,name="sturegister"),
    path('login/',views.login_view,name="login"),
    path('logout/',views.logout_view,name="logout"),
    path('update/<str:un>/',views.update_user,name="update"),

    #auth_views

    #path('password_change/',auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html'),name='password_change'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name="accounts/password_change.html",success_url=reverse_lazy('accounts:password_change_done')), name='password_change'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),

]

