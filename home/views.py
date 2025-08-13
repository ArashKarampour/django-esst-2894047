from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello World!")

def home2(request):
    return HttpResponse("This is the app2")