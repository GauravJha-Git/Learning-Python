numbers = [1,-1,3,-4,5,6,-7,-8,9,10]
positive_number_count = 0
for num in numbers:
    if num > 0:
        positive_number_count += 1
        
print("total positive numbers: ", positive_number_count)