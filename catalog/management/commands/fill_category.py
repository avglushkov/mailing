from django.core.management import BaseCommand
from catalog.models import Product, Category

import json


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('category.json', 'r', encoding="utf-8") as file:
            category_load = file.read()
            categories = json.loads(category_load)
        return categories


    def handle(self, *args, **options):

        Category.objects.all().delete()

        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(pk=category['pk'],
                         category_name=category['fields']['category_name'],
                         category_description=category['fields']['category_description'])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

