from django.shortcuts import render
from django.views.generic import ListView
from app1.models import Users

# Create your views here.
class UsersView(ListView):
    model = Users
    queryset = Users.objects.all()