# delivery_system/models.py
from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=100)

class Item(models.Model):
    PERISHABLE = 'perishable'
    NON_PERISHABLE = 'non-perishable'
    ITEM_TYPES = [
        (PERISHABLE, 'Perishable'),
        (NON_PERISHABLE, 'Non-Perishable'),
    ]
    type = models.CharField(max_length=20, choices=ITEM_TYPES)
    description = models.CharField(max_length=255)

class Pricing(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    zone = models.CharField(max_length=100)
    base_distance_in_km = models.PositiveIntegerField()
    km_price = models.DecimalField(max_digits=5, decimal_places=2)
    fixed_price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = ('organization', 'item', 'zone')
