from django.urls import path, include
from catalog.apps import NewappConfig
from catalog.views import home, contacts, product

app_name = NewappConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products/<int:pk>', product, name='product'),
]
