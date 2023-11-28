from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from app1.models import Tillage, Farm, Harvest
from django.shortcuts import render, get_object_or_404, redirect
from .forms import FarmForm, HarvestForm
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

def harvest_create(request, farm_id):
    farm = get_object_or_404(Farm, pk=farm_id)
    if request.method == 'POST':
        form = HarvestForm(request.POST)
        if form.is_valid():
            harvest = form.save(commit=False)
            harvest.farm = farm  # Associar a lavoura à fazenda
            harvest.save()
            return redirect('app1:farm_detail', pk=farm_id)
    else:
        form = HarvestForm()
    return render(request, 'app1/harvest_form.html', {'form': form, 'farm': farm})