from django.shortcuts import render


def index(request):
    return render(request, 'catalog/home.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'Новое сообщение от пользователя {name}({email}): {message}')
    return render(request, 'catalog/contacts.html')
