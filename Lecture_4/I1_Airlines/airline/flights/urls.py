from . import views
from django.urls import path

urlpatterns =[
    path("",views.index,name="index"),
    
    # https://youtu.be/YzP164YANAU?t=4592
    # for every flight to have its own page
    path("<int:flight_id>",views.flight, name="flight"),

    path("<int:flight_id>/book",views.book, name="book"),

]