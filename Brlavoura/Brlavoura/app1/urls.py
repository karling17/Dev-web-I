from django.urls import path 
from app1 import views

urlpatterns = [
    path('users', views.UsersView.as_view(), name='users')
]