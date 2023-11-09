from django.urls import path 
from app1 import views

app_name = 'brlavoura'

urlpatterns = [
    path('', views.FarmView.as_view(), name='farm'),
    path('', views.UsersView.as_view(), name='users'),
    path('create/', views.UsersCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.UsersUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', views.UsersDelete.as_view(), name='delete'),
    
]