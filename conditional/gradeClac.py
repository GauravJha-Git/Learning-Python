score = int(input("enter your Score: "))

if score > 100:
    print("verify your scores")
    exit()


if score >= 90:
    grade = "A"
elif score>=80:
    grade = "B"
elif score>=70:
    grade = "C"
elif score>=60:
    grade = "D"
else:
    grade = "F"
    
print("your grade is: ", grade)