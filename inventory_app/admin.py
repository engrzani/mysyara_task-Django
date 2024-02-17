from django.contrib import admin

# Register your models here.
# inventory/admin.py
from django.contrib import admin
from .models import InventoryItem, TodayUsage

admin.site.register(InventoryItem)
admin.site.register(TodayUsage)
