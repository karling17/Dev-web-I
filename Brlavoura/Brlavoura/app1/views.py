from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from app1.models import Tillage, Farm, Harvest, Humidity
from django.shortcuts import render, get_object_or_404, redirect
from .forms import FarmForm, HarvestForm, TillageForm
from django.urls import reverse
import random
from django.utils import timezone


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

def harvest_detail(request, farm_id, harvest_id):
    farm = get_object_or_404(Farm, pk=farm_id)
    harvest = get_object_or_404(Harvest, pk=harvest_id, farm=farm)
    # Adicione aqui a lógica para buscar as safras associadas, se necessário
    return render(request, 'app1/harvest_detail.html', {'farm': farm, 'harvest': harvest})

def harvest_delete(request, farm_id, harvest_id):
    farm = get_object_or_404(Farm, pk=farm_id)
    harvest = get_object_or_404(Harvest, pk=harvest_id, farm=farm)
    if request.method == 'POST':
        harvest.delete()
        return redirect('app1:farm_detail', pk=farm_id)
    return render(request, 'app1/harvest_confirm_delete.html', {'farm': farm, 'harvest': harvest})

def tillage_create(request, farm_id, harvest_id):
    harvest = get_object_or_404(Harvest, pk=harvest_id, farm_id=farm_id)
    if request.method == 'POST':
        form = TillageForm(request.POST)
        if form.is_valid():
            tillage = form.save(commit=False)
            tillage.harvestId = harvest  # Certifique-se de que este campo corresponda ao seu modelo
            tillage.save()
            return redirect('app1:harvest_detail', farm_id=farm_id, harvest_id=harvest_id)
    else:
        form = TillageForm()
    return render(request, 'app1/tillage_form.html', {'form': form, 'harvest': harvest})

def add_humidity(request, tillage_id):
    tillage = get_object_or_404(Tillage, pk=tillage_id)
    humidity_value = random.uniform(30, 50)  # Gera um valor aleatório entre 30 e 50
    Humidity.objects.create(tillage_id=tillage_id, humidity=humidity_value, timestamp=timezone.now())

    # Redireciona para a visualização do detalhe da safra
    return redirect('app1:tillage_detail', tillage_id=tillage_id)

def tillage_detail(request, tillage_id):
    tillage = get_object_or_404(Tillage, pk=tillage_id)
    humidities = tillage.humidities.all()  # Usando o related_name definido
    return render(request, 'app1/tillage_detail.html', {'tillage': tillage, 'humidities': humidities})
