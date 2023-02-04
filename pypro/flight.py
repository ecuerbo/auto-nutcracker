class flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers =[]

    def add_passenger(self,name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)
flight = flight(3)

people = ["Luis", "Gina", "Grace", "Leo", "Lex","Luela"]

for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}")