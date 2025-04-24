import math

def circle(radius):
    area = math.pi * (radius**2)
    circumference = 2* math.pi *radius
    
    return area, circumference

print(circle(5))

a,c = circle(8)
print("Area: ",a, "Circumference: ",c)
    