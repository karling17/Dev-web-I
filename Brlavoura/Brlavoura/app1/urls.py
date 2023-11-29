from django.urls import path 
from app1 import views

app_name = 'brlavoura'

urlpatterns = [
    path('farms/', views.farm_list, name='farm_list'),
    path('farms/new/', views.farm_create, name='farm_create'),
    path('farms/<int:pk>/edit/', views.farm_edit, name='farm_edit'),
    path('farms/<int:pk>/delete/', views.farm_delete, name='farm_delete'),
    path('farms/<int:pk>/', views.farm_detail, name='farm_detail'), 
    path('farms/<int:farm_id>/create_harvest/', views.harvest_create, name='harvest_create'),
    path('farms/<int:farm_id>/harvests/<int:harvest_id>/', views.harvest_detail, name='harvest_detail'),
    path('farms/<int:farm_id>/harvests/<int:harvest_id>/delete/', views.harvest_delete, name='harvest_delete'),
]