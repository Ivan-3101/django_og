from django.shortcuts import render


#creating global variable
tasks = ["foo","bar","baz"]

# Create your views here.
def index(request):
    return render(request,"tasks/index.html",{
        "tasks": tasks
        #key the html template has access to : values the var takes on
    })

def add(request):
    return render(request,"tasks/add.html")