class Car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model
    
    def get_brand(self):
        return self.__brand + "!"
    
    def fullName(self):
        
        return f"{self.brand} {self.model}" #this is a formated string
class ElectricCar(Car):
    def __init__(self,brand,model,batterySize):
        super().__init__(brand,model)
        self.batterySize = batterySize
        
mycar = Car("Tesla","Model S")

print(mycar.get_brand())