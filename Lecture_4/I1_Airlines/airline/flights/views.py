from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect

from .models import Flight,Airport,Passenger

from django.urls import reverse
# Create your views here.

def index(request):
    # return HttpResponse("Praise the Lord")
    return render(request, "flights/index.html",{
        "flights" : Flight.objects.all()
    })

def flight(request,flight_id):
    # first step is getting the fligh
    # whose id is entered 
    flight = Flight.objects.get(id=flight_id)
    # pk for primary key, id= flight is also ok

    passengers = flight.passengers.all()
    non_passengers = Passenger.objects.exclude(flights=flight).all()

    return render(request,"flights/flight.html",{
        "flight" : flight,
        "passengers" : passengers,
        "non_passengers" : non_passengers,
    })


def book(request,flight_id):
    # https://youtu.be/YzP164YANAU?t=5190
    # we use post whenever we send data to the page
    # whenever we manipulate the state of something or database
    # we use "POST"
    if request.method == "POST":
        # getting the flight requested whose pk is that flight_id
        flight = Flight.objects.get(pk=flight_id)
        # recall that .get is used whenever we know that only one result will be obtained

        # Whenver someone submits the form
        # we need the flight and passenger info to book the flight
        passenger_id = int(request.POST["passenger"])
        passenger = Passenger.objects.get(pk=passenger_id)
        # What this means is that the data about which passenger ID we want to register on this flight is going
        # to be passed in via a form with an input field whose name is passenger. The name on any particular input field dictates what name we get--
        # is received when a route like this book route is able to process the request from the user.\

        # So now what I've done is, if the request method is post, meaning someone submitted this form via the post request method,
        # I'm first thing flights.objects.get. to get a particular flight, get me the flight with that flight ID.
        # And then, I'm getting a passenger. Which passenger am I getting? The one who's pk, their primary key, otherwise known as ID,
        # is equal to whatever was submitted via this post form with a name of passenger.

        passenger.flights.add(flight)
        # let's just assume for now that we're able to get a flight
        # and get a passenger. Well, how do we access a passenger's flights? I can just say passenger.flights.

        return HttpResponseRedirect(reverse("flight",args=(flight.id,)))

