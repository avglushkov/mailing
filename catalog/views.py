from django.shortcuts import render, get_object_or_404
from django import template
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.core.mail import send_mail
from django.forms import inlineformset_factory
from pytils.translit import slugify
from django.contrib.auth.mixins import LoginRequiredMixin
from catalog.models import Product, Contact, Version
from catalog.forms import ProductForm, ContactForm, VersionForm


# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    extra_context = {'title':'Каталог продуктов'}

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data( *args,**kwargs)
        actual_versions = Version.objects.filter(actual_version=True)
        context_data['actual_version'] = actual_versions

        return context_data


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'
    extra_context = {'title': 'Информация о продукте'}



class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
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
    success_url = reverse_lazy('catalog:home')
    extra_context = {'title': 'Изменение продукта'}


class ContactCreateView(CreateView):
    model = Contact
    template_name = 'catalog/contacts.html'
    form_class = ContactForm
    success_url = reverse_lazy('catalog:home')
    extra_context = {'title': 'Добавление контакта'}




