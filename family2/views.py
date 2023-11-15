from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def nani(request):
    return HttpResponse('<h1>gnanendra</h1>')

def gnaneswari(request):
    return HttpResponse('<h1>wife of gnanendra</h1>')