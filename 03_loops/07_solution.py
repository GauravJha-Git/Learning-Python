while True:
    num = int(input("Enter a number : ")) #we want a number between 1 to 10 if not provided then ask again
    if num >= 1 and num<=10 : #we can also write this like 1=< num <=10
        print("Thanks")
        break
    else:
        print("Invalid number, try again")