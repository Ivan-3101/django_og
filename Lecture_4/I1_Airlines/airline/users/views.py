from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import authenticate,login,logout
# Create your views here.

# display info about the currently signed in user   
# If no user is signed in, return to login page:
def index(request):
    # The request object that gets passed in as part of the request to every user in Django automatically has
    # a user attribute associated with it. And that user object has an is authenticated attribute that tells us
    # if the user is signed in or not.    if not request.user.is_authenticated:
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request,"users/user.html")


def login_view(request):
    if request.method == "POST":
        # Accessing username and password from form data
        # request.POST["username"] since we gave the name="username"/"password" in the html form
        username = request.POST["username"]
        password = request.POST["password"]

        # Check if username and password are correct, returning User object if so
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # if authentication is successful
            login(request,user)
            return HttpResponseRedirect(reverse("index"))
        else:
            # if authentication fails
            return render(request,"users/login.html",{
                "message": "Invalid Credentials.",
            })

    return render(request,"users/login.html",)

def logout_view(request):
    # calls the logout function as we imported it
    logout(request)
    return render(request, "users/login.html", {
                "message": "Logged Out."
            })