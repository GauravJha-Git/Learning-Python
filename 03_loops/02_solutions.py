numbers = int(input("Enter a number : "))

total=0

for i in range(0 , numbers+1):
    if(i % 2 == 0):
        total += i
        
print("Total count :", total)
    