class vehical:
    def __init__(self, seating):
        self.seating = seating

    def fare(self):
        return  self.seating * 100


class bus(vehical):

    def fare(self):
        total_fare = super().fare()
        maintance = total_fare *0.10
        return total_fare + maintance


b = bus(50)
print(b.fare())

        

class vehical:

    def seating_capacity(self,capacity):

        return f"The seating capacity of a vehicle is {capacity} passengers"



class bus(vehical):

    def seating_capacity(self, capacity =50):
        return super().seating_capacity(capacity)


b = bus()

print(b.seating_capacity())
    
        
        