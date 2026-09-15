from django.core.management import BaseCommand
from inventory.models import Category, Item


class Command(BaseCommand):
    help = "Category and Item data to be seeded in database."

    def handle(self, *args, **kwargs):

        categories = [
            {
                "name": "Electronics",
                "description": "Electronic products",
            },
            {
                "name": "Furniture",
                "description": "Furniture products",
            },
            {
                "name": "Stationery",
                "description": "Stationery products",
            },
        ]

        created_category = Category.objects.bulk_create(
            Category(**category) for category in categories
        )

        electronics = created_category[0]
        furniture = created_category[1]
        stationery = created_category[2]

        items = [
            {
                "sku": "ELEC001",
                "name": "Wireless Mouse",
                "quantity_on_hand": 25,
                "unit_price": 1500,
                "category": electronics,
            },
            {
                "sku": "ELEC002",
                "name": "Keyboard",
                "quantity_on_hand": 15,
                "unit_price": 2500,
                "category": electronics,
            },
            {
                "sku": "FURN001",
                "name": "Office Chair",
                "quantity_on_hand": 10,
                "unit_price": 8500,
                "category": furniture,
            },
            {
                "sku": "STAT001",
                "name": "Notebook",
                "quantity_on_hand": 50,
                "unit_price": 250,
                "category": stationery,
            },
        ]

        Item.objects.bulk_create(
            Item(**item) for item in items
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"{len(categories)} categories and "
                f"{len(items)} items seeded successfully."
            )
        )