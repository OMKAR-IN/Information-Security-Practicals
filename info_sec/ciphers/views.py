from django.shortcuts import render

def home_ciphers(request):
    return render(request, 'ciphers/home.html', {})
