from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login, name='student_login'),
    path('test', views.exam_test)
]
