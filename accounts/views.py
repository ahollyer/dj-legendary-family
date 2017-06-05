from django.shortcuts import render, HttpResponse

def home(request):
    numbers = [1, 2, 3, 4, 5]
    name = 'Aspen'
    context = {
        'name': name,
        'numbers': numbers,
    }
    return render(request, 'accounts/home.html', context)
