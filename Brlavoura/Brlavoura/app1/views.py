from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from app1.models import Farm, Users

# Create your views here.
class UsersView(ListView):
    model = Users
    queryset = Users.objects.all()
    context_object_name = 'users'

class  UsersCreate(CreateView):
    model = Users
    fields = '__all__'
    success_url = reverse_lazy('brlavoura:users')

class UsersUpdate(UpdateView): 
    model = Users
    fields = '__all__'
    success_url = reverse_lazy('brlavoura:users')

class UsersDelete(DeleteView):
    queryset = Users.objects.all()
    success_url = reverse_lazy('brlavoura:users')

class FarmView(ListView):
    model = Farm
    queryset = Farm.objects.all()
    context_object_name = 'Farms'


