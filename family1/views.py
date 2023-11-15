from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def gnaneswari(request):
    return HttpResponse('<h1>gnaneswari</h1>')

def hari(request):
    return HttpResponse('<h1>hari</h1>')