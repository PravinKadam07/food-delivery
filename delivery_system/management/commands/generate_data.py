from django.core.management.base import BaseCommand
from delivery_system.models import Organization, Item, Pricing
import random

class Command(BaseCommand):
    help = 'Generates sample data for food delivery app'

    def handle(self, *args, **kwargs):
        # Generate sample organizations
        for i in range(5):
            organization = Organization.objects.create(name=f'Organization {i+1}')

        # Generate sample items
        for i in range(10):
            item_type = random.choice(['perishable', 'non-perishable'])
            description = f'Description {i+1}'
            item = Item.objects.create(type=item_type, description=description)

        # Generate sample pricing
        for organization in Organization.objects.all():
            for item in Item.objects.all():
                for zone in ['central', 'north', 'south']:
                    base_distance = random.randint(3, 8)
                    km_price = round(random.uniform(1, 2), 2)
                    fixed_price = round(random.uniform(8, 15), 2)
                    Pricing.objects.create(
                        organization=organization,
                        item=item,
                        zone=zone,
                        base_distance_in_km=base_distance,
                        km_price=km_price,
                        fixed_price=fixed_price
                    )

        self.stdout.write(self.style.SUCCESS('Sample data generated successfully!'))
