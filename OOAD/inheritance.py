class Vehicle:
    company="Hyundai Motors"
    def __init__(self,n_wheels,n_seats,mileage):
        self.n_wheels=n_wheels
        self.n_seats=n_seats
        self.mileage=mileage
    def get_vehicle_details(self):
        return f"This vehicle has {self.n_wheels} number of wheels, {self.n_seats} seats and provides a mileage of {self.mileage}"

class Car(Vehicle):
    # def __init__(self,make,company,colour):
    pass
c1=Car(4,5,20)


v1=Vehicle(10,5,"10")
# print(v1.get_vehicle_details())
print(c1.get_vehicle_details())