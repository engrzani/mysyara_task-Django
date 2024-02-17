# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import InventoryItem, TodayUsage
from .forms import InventoryItemForm, TodayUsageForm

def index(request):
    return render(request, 'index.html')
def inventory_list(request):
    inventory_items = InventoryItem.objects.all()
    return render(request, 'inventory_list.html', {'inventory_items': inventory_items})

def inventory_detail(request, pk):
    inventory_item = get_object_or_404(InventoryItem, pk=pk)
    return render(request, 'inventory_detail.html', {'inventory_item': inventory_item})

def inventory_create(request):
    if request.method == 'POST':
        form = InventoryItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = InventoryItemForm()
    return render(request, 'inventory_form.html', {'form': form})

def inventory_update(request, pk):
    inventory_item = get_object_or_404(InventoryItem, pk=pk)
    if request.method == 'POST':
        form = InventoryItemForm(request.POST, instance=inventory_item)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = InventoryItemForm(instance=inventory_item)
    return render(request, 'inventory_form.html', {'form': form})

def inventory_delete(request, pk):
    inventory_item = get_object_or_404(InventoryItem, pk=pk)
    if request.method == 'POST':
        inventory_item.delete()
        return redirect('inventory_list')
    return render(request, 'inventory_confirm_delete.html', {'inventory_item': inventory_item})

def today_usage_list(request):
    today_usage = TodayUsage.objects.all()
    return render(request, 'today_usage_list.html', {'today_usage': today_usage})

def today_usage_create(request):
    if request.method == 'POST':
        form = TodayUsageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('today_usage_list')
    else:
        form = TodayUsageForm()
    return render(request, 'today_usage_form.html', {'form': form})
