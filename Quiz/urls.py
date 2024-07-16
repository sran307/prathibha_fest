from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('quiz_master',views.quizMaster, name='quiz_master'),
    path('class_list',views.classList, name='classList'),
    path('save_classlist', views.saveClasslist, name='save_classlist'),
]