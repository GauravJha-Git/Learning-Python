class Car:
    
    total_car=0
    
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model
        Car.total_car+=1
    
    def get_brand(self):
        return self.__brand + "!"
    
    def fullName(self):        
        return f"{self.brand} {self.model}" #this is a formated string
    
    def fuel_type(self):
        return "petrol or diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
class ElectricCar(Car):
    def __init__(self,brand,model,batterySize):
        super().__init__(brand,model)
        self.batterySize = batterySize
        
    def fuel_type(self):
        return "Electric Charge"
    
my_tesla = ElectricCar("Tesla","Model S" ,"85kWh")
print(my_tesla.fuel_type())

safari = Car("Tata","Safari")
print(safari.fuel_type())

# print(safari.general_description())
print(Car.general_description())

print(Car.total_car)