from django.urls import path
from .import views

urlpatterns = [
    path('get/', views.courselist, name="get_course"),
    path('course/<str:cn>', views.coursemodule, name='modules',),
    path('create/', views.createcourse, name='create'),
]
