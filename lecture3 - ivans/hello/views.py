from django.http import HttpResponse
# to import HttpResponse
from django.shortcuts import render

# Create your views here.

# def index(request):
#        # return HttpResponse("Hello, world!!")
#        return HttpResponse("<h1>Praise the Lord!!!</h1>")

def index(request):
      return render(request,"hello/index.html")
# instead of writing entire html codes we render the html page
# aka a template
# https://youtu.be/w8q0C-C1js4?t=1749

def ivan(request):
    return HttpResponse("<h2>Hello, Ivan!</h2>")

def diana(request):
       return HttpResponse("<h2>Hello, Diana!</h2>")

def alfred(request):
      return HttpResponse("Hello, Dad!")

def greet(request,name):
       # return HttpResponse(f"<h3>Hello, {name.capitalize()}!</h3>")
       return render(request,"hello/greet.html",
              {
                     "name":name.capitalize()
              })
       # dictionaries are ordered, changeable and do not allow duplicates
       # https://youtu.be/w8q0C-C1js4?t=1938


