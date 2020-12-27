from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    return render(request, 'Jutka/index.html')

def elso(request):
        return render(request, 'Jutka/elso.html')

def masodik(request):
            return render(request, 'Jutka/masodik.html')

def harmadik(request):
                return render(request, 'Jutka/harmadik.html')

# Create your views here.
