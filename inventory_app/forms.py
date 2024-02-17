# forms.py
from django import forms
from .models import InventoryItem, TodayUsage

class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ['serial_no', 'part_number', 'description', 'brand', 'quantity', 'price']

class TodayUsageForm(forms.ModelForm):
    class Meta:
        model = TodayUsage
        fields = ['sr_no', 'item', 'part_number', 'mechanic', 'quantity', 'model']
