
from django.conf import settings
from django.core.cache import cache
from catalog.models import Category, Product



def get_category_list():
    """ Берем из кэша список категорий, если кэш пуст, то записываем список категорий в БД"""

    if settings.CACHE_ENABLED:
        key = 'category_list'
        categories = cache.get(key)
        if categories is None:
            categories = Category.objects.all()
            cache.set(key, categories)
    else:
        categories = Category.objects.all()
    return categories


def get_product_list():
    """ Берем из кэша список продуктов, если кэш пуст, то записываем список продуктов в БД"""

    if settings.CACHE_ENABLED:
        key = 'product_list'
        products = cache.get(key)
        if products is None:
            products = Product.objects.all()
            cache.set(key, products)
    else:
        products = Product.objects.all()
    return products