# urls.py (inside the main project directory)
from django.urls import path
from .views import index,inventory_create,inventory_delete,inventory_detail,inventory_list,inventory_update,today_usage_create,today_usage_list,InventoryItem

urlpatterns = [
    path('',index, name='index'),
    path('inventory/',inventory_list, name='inventory_list'),
    path('inventory/<int:pk>/', inventory_detail, name='inventory_detail'),
    path('inventory/create/', inventory_create, name='inventory_create'),
    path('inventory/<int:pk>/update/', inventory_update, name='inventory_update'),
    path('inventory/<int:pk>/delete/', inventory_delete, name='inventory_delete'),
    path('list/',today_usage_list, name='today_usage_list'),
    path('create/', today_usage_create, name='today_usage_create'),

]
