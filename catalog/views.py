from django.shortcuts import render, get_object_or_404
from catalog.models import Product, Contact, Blog
from django import template
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify
from django.core.mail import send_mail


# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'


class ContactCreateView(CreateView):
    model = Contact
    template_name = 'catalog/contacts.html'
    fields = '__all__'
    success_url = reverse_lazy('catalog:home')


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(published=True)

        return queryset


class BlogCreateView(CreateView):
    model = Blog
    fields = '__all__'
    success_url = reverse_lazy('catalog:blog_list')

    def form_valid(self, form):
        new_blog = form.save()
        new_blog.slug = slugify(new_blog.header)
        new_blog.save()

        return super().form_valid(form)


class BlogDetailView(DetailView):
    model = Blog
    fields = '__all__'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()

        if self.object.views_count == 100:
            subject = f'{self.object.header} - очень популярный блог'
            message = f'Количество просмотров блога {self.object.header} превысило 100'
            from_email = 'djangopost@yandex.ru'
            recipient_list = ['avgl@mail.ru']
            send_mail(subject, message, from_email, recipient_list,fail_silently=False)

        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = '__all__'

    # success_url = reverse_lazy('catalog:blog_list')

    def form_valid(self, form):
        new_blog = form.save()
        new_blog.slug = slugify(new_blog.header)
        new_blog.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_list')

