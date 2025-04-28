age = int(input("Enter Your age:"))
day = input("enter day: ")

price = 12 if age>=18 else 8

if day == "wednesday":
    price = price-2
    # price -=2


print("Ticket Price for you is $",price)
