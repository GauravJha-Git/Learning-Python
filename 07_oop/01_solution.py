class Car:
    def __init__(self, userbrand , usermodel):
        
        self.brand = userbrand
        self.model = usermodel
    
my_car = Car("Toyota","Hilux")
print(my_car.brand)
print(my_car.model)

my_car2 = Car("Rolls Royace","Phantom")

print(my_car2.model)
print(my_car2.brand)
