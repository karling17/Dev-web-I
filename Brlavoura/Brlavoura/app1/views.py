from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from app1.models import Farm
from django.shortcuts import render, get_object_or_404, redirect
from .forms import FarmForm
from django.urls import reverse


# Create your views here.

def farm_list(request):
    farms = Farm.objects.all()
    return render(request, 'app1/farm_list.html', {'farms': farms})

def farm_create(request):
    if request.method == 'POST':
        form = FarmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/farms')
    else:
        form = FarmForm()
    return render(request, 'app1/farm_form.html', {'form': form})

def farm_edit(request, pk):
    farm = get_object_or_404(Farm, pk=pk)
    if request.method == 'POST':
        form = FarmForm(request.POST, instance=farm)
        if form.is_valid():
            form.save()
            return redirect('farm_list')
    else:
        form = FarmForm(instance=farm)
    return render(request, 'app1/farm_form.html', {'form': form})


def farm_delete(request, pk):
    farm = get_object_or_404(Farm, pk=pk)
    if request.method == 'POST':
        farm.delete()
        return redirect('/farms/')
    return render(request, 'app1/farm_confirm_delete.html', {'farm': farm})

def farm_detail(request, pk):
    farm = get_object_or_404(Farm, pk=pk)
    return render(request, 'app1/farm_detail.html', {'farm': farm})


