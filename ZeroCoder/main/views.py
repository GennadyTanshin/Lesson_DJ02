from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def new(request):
    return render(request, 'main/new.html')

def test(request):
    return HttpResponse("<h1>Это страница TEST моего проекта на  Django</h1>")