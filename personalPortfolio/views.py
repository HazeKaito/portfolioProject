from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mainpage(request):
    return render(request, 'personalPortfolio/mainpage.html')

def contacts(request):
    return render(request, 'personalPortfolio/contacts.html')

def projectpage(request):
    return render(request, 'personalPortfolio/projectpage.html')