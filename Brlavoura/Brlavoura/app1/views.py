from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from app1.models import Farm

# Create your views here.

class FarmView(ListView):
    model = Farm
    queryset = Farm.objects.all()
    context_object_name = 'Farms'


