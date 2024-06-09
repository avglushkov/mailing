from django.core.management import BaseCommand
from catalog.models import Product, Category

import json


class Command(BaseCommand):

    # @staticmethod
    # def json_read_categories():
    #     with open('category.json', 'r', encoding="utf-8") as file:
    #         category_load = file.read()
    #         categories = json.loads(category_load)
    #     return categories

    @staticmethod
    def json_read_products():
        with open('product.json', 'rt', encoding="utf-8") as file:
            products_load = file.read()
            products = json.loads(products_load)
        return products

    def handle(self, *args, **options):
        # Category.objects.all().delete()
        Product.objects.all().delete()

        product_for_create = []
        # category_for_create = []

        # # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        # for category in Command.json_read_categories():
        #     category_for_create.append(
        #         Category(pk=category['pk'],
        #                  category=category['fields']['category'],
        #                  category_description=category['fields']['category_description'])
        #     )
        #
        # # Создаем объекты в базе с помощью метода bulk_create()
        # Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
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
            #
            #
            # product_for_create.append(
            #     Product(name=product['fields']['name'],
            #             description=product['fields']['description'],
            #             category=Category.objects.get(pk=product['fields']['category']),
            #             price=product['fields']['price']
            #             )
            # )
            # for product in Command.json_read('catalog_product_data.json'):
            # product_for_create.append(Product(pk=product['pk'],
            #                                   name=product['fields']['name'],
            #                                   description=product['fields']['description'],
            #                                   preview=product['fields']['preview'],
            #                                   category=Category.objects.get(pk=product['fields']['category']),
            #                                   price=product['fields']['price'],
            #                                   created_at=product['fields']['created_at'],
            #                                   updated_at=product['fields']['updated_at']
            #                                   ))

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
