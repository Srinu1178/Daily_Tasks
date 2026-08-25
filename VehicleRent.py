class Vehicle:
    def __init__(self,vehicle_id,brand,model,rent_per_days,available):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.rent_per_days = rent_per_days
        self.available = available
    def rent(self):
        if self.available:
            self.available-=1
            print(f"Rent the Vehicle:{self.vehicle_id}")
        else:
            print("Vehicles are not available")
    
    def return_vehicle(self):
        self.available+=1
        print(f'Vehicle is returned {self.vehicle_id}')

    def calculate_rent(self,days):
        return self.rent_per_days * days

    def display_details(self):
        print(f'Vehicle No: {self.vehicle_id}')
        print(f'Vehicle Brand: {self.brand}')
        print(f'Vehicle Model: {self.model}')
        print(f'Vehicle base rent: {self.rent_per_days}')
        print(f'Vehicle avialables : {self.available}')

class Car(Vehicle):
    def __init__(self,vehicle_id,brand,model,rent_per_days,available,insurance_charge):
        super().__init__(vehicle_id,brand,model,rent_per_days,available)
        self.insurance_charge = insurance_charge

    def calculate_rent(self, days):
        return self.insurance_charge + super().calculate_rent(days)

    def display_details(self):
        super().display_details()
        print(f'The vehicle is Car')
        print(f'Insurance_charge:{self.insurance_charge}')



class Bike(Vehicle):
   def __init__(self,vehicle_id,brand,model,rent_per_days,available,helmet_charge):
        super().__init__(vehicle_id,brand,model,rent_per_days,available)
        self.helmet_charge = helmet_charge

   def calculate_rent(self, days):
        return self.helmet_charge + super().calculate_rent(days)
   
   def display_details(self):
        super().display_details()
        print(f'The vehicle is Bike')
        print(f'Add Helmet_charge:{self.helmet_charge}')
   

class Truck(Vehicle):
   def __init__(self,vehicle_id,brand,model,rent_per_days,available,load_capacity):
        super().__init__(vehicle_id,brand,model,rent_per_days,available)
        self.load_capacity = load_capacity

   def calculate_rent(self, days):
       load_charge = self.load_capacity * 300 * days
       return super().calculate_rent(days)+load_charge



   def display_details(self):
        super().display_details()
        print(f'The vehicle is Truck')
        print(f'Truck specification:{self.load_capacity}')



veh1 = Vehicle(101,'haridevason',2025,3,4)
veh1.display_details()
veh1.rent()
veh1.display_details()
veh1.return_vehicle()
veh1.display_details()

car1 = Car(102,'RangeRover',2021,3000,1,500)
print("--"*30)
car1.display_details()
car1.rent()
car1.display_details()
print(car1.calculate_rent(4))

bike1 = Bike(301,'Duke',2021,1500,3,300)
print("----"*40)
bike1.display_details()
bike1.rent()
print(f'The bike rent for 3 days {bike1.calculate_rent(3)}')

