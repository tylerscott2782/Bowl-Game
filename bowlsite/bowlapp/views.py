from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return HttpResponseRedirect(reverse("bowlapp:login"))

def login(request):
    return render(request, "bowlapp/login.html")

def createaccount(request):
        if request.method == "POST":
            try:
                email = request.POST["email"]
                password = request.POST["password"]
                retyped_password = request.POST["retyped_password"]
                if password != retyped_password:
                    return HttpResponse("password did not match retyped password")
                User.objects.create_user("user", email, password)
                return HttpResponseRedirect(reverse("bowlapp:login"))
            except:
                return HttpResponseRedirect(reverse("bowlapp:createaccount"))
        else:
            return render(request, "bowlapp/createaccount.html")

def overview(request):
    return HttpResponse("overview")