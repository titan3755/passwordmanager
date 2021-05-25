from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('about/', views.about, name='about'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.register, name='register'),
    path('passwords/', views.passwords, name='passwords'),
    path('logout/', views.logoutUser, name='logout'),
    path('view/', views.viewPassword, name='viewpass'),
    path('delete/', views.deleteEntry, name='delete'),
    path('update/', views.updateEntry, name='update'),
]