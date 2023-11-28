from django.urls import path 
from app1 import views

app_name = 'brlavoura'

urlpatterns = [
    path('', views.FarmView.as_view(), name='farm'),
    
    
]