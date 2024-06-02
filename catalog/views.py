from django.shortcuts import render


# Create your views here.
def home(request):

    return render(request, 'home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name}({email}, {phone}): {message}')

    return render(request, 'contacts.html')

