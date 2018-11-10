from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def mainPage(request):
    return render(request, 'mainPage.html',{})