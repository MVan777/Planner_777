from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.login, name='login'),
    path('register/', views.register, name='register'),
]