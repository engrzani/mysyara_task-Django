from django.db import models

class InventoryItem(models.Model):
    serial_no = models.CharField(max_length=50)
    part_number = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    brand = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class TodayUsage(models.Model):
    sr_no = models.CharField(max_length=50)
    item = models.CharField(max_length=255)
    part_number = models.CharField(max_length=50)
    mechanic = models.CharField(max_length=100)
    quantity = models.IntegerField()
    model = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
