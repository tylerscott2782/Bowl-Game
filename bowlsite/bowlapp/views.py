from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def index(request):
    return HttpResponseRedirect(reverse("bowlapp:login"))

def login(request):
    return render(request, "bowlapp/login.html")

def createaccount(request):
    return render(request, "bowlapp/createaccount.html")

def overview(request):
    return HttpResponse("overview")