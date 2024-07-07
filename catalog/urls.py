from django.urls import path, include
from catalog.apps import NewappConfig
from catalog.views import ProductListView, ProductDetailView, ContactCreateView, ProductCreateView, ProductUpdateView

app_name = NewappConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactCreateView.as_view(), name='contacts'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('product_update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),

]

