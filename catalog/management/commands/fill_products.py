from django.core.management import BaseCommand
from catalog.models import Product, Category

import json


class Command(BaseCommand):

   @staticmethod
    def json_read_products():
        with open('product.json', 'rt', encoding="utf-8") as file:
            products_load = file.read()
            products = json.loads(products_load)
        return products

    def handle(self, *args, **options):
        Product.objects.all().delete()

        product_for_create = []

        for product in Command.json_read_products():
            product_for_create.append(Product(pk=product['pk'],
                                              name=product['fields']['name'],
                                              description=product['fields']['description'],
                                              image=product['fields']['image'],
                                              category=Category.objects.get(pk=product['fields']['category']),
                                              price=product['fields']['price'],
                                              created_at=product['fields']['created_at'],
                                              updated_at=product['fields']['updated_at']
                                              ))

    Product.objects.bulk_create(product_for_create)
