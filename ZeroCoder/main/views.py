from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Это мой первый проект на Django</h1>")

def data(request):
    return HttpResponse("<h1>Это страница DATA моего проекта на  Django</h1>")

def test(request):
    return HttpResponse("<h1>Это страница TEST моего проекта на  Django</h1>")