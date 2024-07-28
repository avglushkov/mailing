from django.shortcuts import render, get_object_or_404
from django import template
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.core.mail import send_mail
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from pytils.translit import slugify
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

from catalog.models import Product, Contact, Version, Category
from catalog.forms import ProductForm, ContactForm, VersionForm, ProductModeratorsForm
from catalog.services import get_category_list, get_product_list


# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    extra_context = {'title': 'Каталог продуктов'}

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        actual_versions = Version.objects.filter(actual_version=True)
        context_data['actual_version'] = actual_versions
        context_data['product_list'] = get_product_list()


        return context_data


# @login_required
class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'
    extra_context = {'title': 'Информация о продукте'}


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.add_product'
    success_url = reverse_lazy('catalog:home')
    extra_context = {'title': 'Добавление продукта'}

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.change_product'
    success_url = reverse_lazy('catalog:home')
    extra_context = {'title': 'Изменение продукта'}

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        elif user.has_perm('can_change_publication_status') and user.has_perm(
                'can_change_description') and user.has_perm('can_change_category'):
            print(self.object.owner)
            print(user)
            return ProductModeratorsForm
        else:

            raise PermissionDenied



class ContactCreateView(CreateView):
    model = Contact
    template_name = 'catalog/contacts.html'
    form_class = ContactForm
    success_url = reverse_lazy('catalog:home')
    extra_context = {'title': 'Добавление контакта'}

class CategoryListView(ListView):
    model = Category
    # template_name = 'catalog/category_list'
    extra_context = {'title': 'Категории продуктов'}


    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['category_list'] = get_category_list()

        return context_data


