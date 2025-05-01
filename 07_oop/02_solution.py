class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    
    def fullName(self):
        
        return f"{self.brand} {self.model}" #this is a formated string
    
my_car = Car("Toyota","Hilux")

print(my_car.fullName())
        