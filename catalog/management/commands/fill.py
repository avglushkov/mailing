from django.core.management import BaseCommand
from catalog.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        products_list = [
            {'name': 'HP LJ 1100', 'description': 'Old pinter', 'price': 10},
            {'name': 'DJ 333', 'description': '&&&', 'price': 22},
            {'name': 'Проектор', 'description': '%%%', 'price': 1212},
            {'name': 'Сканер1', 'description': 'Сканер1', 'price': 11},
            {'name': 'Сканер2', 'description': 'Сканер2', 'price': 11}
        ]

        Product.objects.all().delete()
        products_for_fill = []
        for prod in products_list:
            products_for_fill.append(Product(**prod))

        print(products_for_fill)
        Product.objects.bulk_create(products_for_fill)