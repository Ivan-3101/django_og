from django.db import models

# Create your models here.


class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"


class Flight(models.Model):
    # origin = models.CharField(max_length=64)
    # https://youtu.be/YzP164YANAU?t=3610
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    # destination = models.CharField(max_length=64)
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE,related_name="arrivals")
    duration = models.IntegerField()

    # returns string representation of the model
    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
    

class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    # https://youtu.be/YzP164YANAU?t=4802
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")
    # m to n relation with flights and passenger
    # every passenger has flights associated with them, which are
    # a models.manytomanyfield with flight. So every passenger could be associated with many flights.

    # blank = "true" : it is possible that a passenger has no flights at all
    # related_name="passengers"
    # if i have a passenger i can use flights attribute to get all of his flights
    # and likewise for flight we can get all the passengers on the flight

    def __str__(self):
        return f"{self.first} {self.last}"