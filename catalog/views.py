from django.shortcuts import render, get_object_or_404
from catalog.models import Product, Contact, Category
from django import template


# Create your views here.
def home(request):
    product_list = Product.objects.all()

    context = {
        'object_list': product_list,
        'title': 'Главная'
    }
    return render(request, 'home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name}({email}, {phone}): {message}')

    context = {
        'title': 'Контакты'
    }

    return render(request, 'contacts.html', context)


def product(request, pk):

    product = get_object_or_404(Product,pk=pk)
    context = {
        'product': product,
        'title': 'Продукт'
    }

    return render(request, 'product.html', context)
