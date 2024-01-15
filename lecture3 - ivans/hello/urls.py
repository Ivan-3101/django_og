from django.urls import path

from . import views

urlpatterns = [
    path("",views.index,name="index"),
    # when some1 visits just the default route
    # on this application
    # go ahead and run the index function

    path("ivan",views.ivan,name="ivan"),
    path("diana",views.diana, name="diana"),

    path("<str:name>",views.greet,name="greet"),
    
    # updated on july 1
    path("Alfred",views.alfred,name="Dad")
]