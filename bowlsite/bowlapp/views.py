from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
def index(request):
    return HttpResponseRedirect(reverse("bowlapp:login"))

def login(request):
    if request.method == "POST":
        try:
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(username=email, password=password)
            if user is not None:
                return HttpResponse("You have been authenticated!")
            return HttpResponseRedirect(reverse("bowlapp:login"))
        except:
            return HttpResponseRedirect(reverse("bowlapp:login"))
    else:
        return render(request, "bowlapp/login.html")

def createaccount(request):
    if request.method == "POST":
        try:
            email = request.POST["email"]
            password = request.POST["password"]
            retyped_password = request.POST["retyped_password"]
            if User.objects.filter(email=email).exists():
                return render(
                    request,
                    "bowlapp/createaccount.html",
                    {
                        "error_message": "There is already an account using that email",
                    },
                )
            if password != retyped_password:
                return render(
                    request,
                    "bowlapp/createaccount.html",
                    {
                        "error_message": "The password did not match the retyped password",
                    },
                )
            new_user = User.objects.create_user(username=email, email=email, password=password)
            new_user.save()
            return HttpResponseRedirect(reverse("bowlapp:login"))
        except:
            return HttpResponseRedirect(reverse("bowlapp:createaccount"))
    else:
        return render(request, "bowlapp/createaccount.html")

def overview(request):
    return HttpResponse("overview")