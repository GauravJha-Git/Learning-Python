input_str = "python"
reversed_str=""
# string is almost treated as list in python

for char in input_str:
    reversed_str = char + reversed_str
    
print("Reversed String : " , reversed_str)