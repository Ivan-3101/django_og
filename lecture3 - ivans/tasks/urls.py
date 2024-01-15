from django.urls import path

from . import views

urlpatterns = [
    path("",views.index,name="index"),
    
    path("add",views.add,name="add"),
    # when we go at tasks/add it will call this view
]