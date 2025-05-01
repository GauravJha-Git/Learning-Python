class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    
    def fullName(self):
        
        return f"{self.brand} {self.model}" #this is a formated string
class ElectricCar(Car):
    def __init__(self,brand,model,batterySize):
        super().__init__(brand,model)
        self.batterySize = batterySize
        
        
myCar = ElectricCar("Tesla","Model s","85kWH")
print(myCar.fullName())
print(myCar.batterySize)
        