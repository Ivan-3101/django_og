class Flight:
    def __init__(self,capacity):
        self.capacity = capacity
        self.passenger_list=[]
    
    def add_passengers(self,name):
        if not self.ifSeatsAvailable():
            return False
            # return (f"Capacity Reached, can't add {self.name}")
        else:
            self.passenger_list.append(name)
            return True
        
    def ifSeatsAvailable(self):
        return self.capacity - len(self.passenger_list)
    
    def printList(self):
        print(self.passenger_list)


air_india = Flight(capacity=2)

people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    if air_india.add_passengers(person):
        print(f"Added {person} to flight.")
    else:
        print(f"No available seats for {person}.")

air_india.printList()
# print(air_india.ifSeatsAvailable())


# class Flight:

#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.passengers = []

#     def add_passenger(self, name):
#         if not self.open_seats():
#             return False
#         self.passengers.append(name)
#         return True

#     def open_seats(self):
#         return self.capacity - len(self.passengers)


# flight = Flight(capacity=3)

# people = ["Harry", "Ron", "Hermione", "Ginny"]
# for person in people:
#     if flight.add_passenger(person):
#         print(f"Added {person} to flight.")
#     else:
#         print(f"No available seats for {person}.")
