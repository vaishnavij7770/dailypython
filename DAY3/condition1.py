#elif statement

marks = 85

if marks<60:
    print("Grade: D")
elif marks<70:
    print("Grade: C")
elif marks<80:
    print("Grade: B")
elif marks<90:
    print("Grade: A")
elif marks<=100:
    print("Grade: A+")
else:
    print("Grade: F")

age = 25
if age<13:
    print("Child")
elif age<20:
    print("Teenager")
elif age<65:
    print("Adult")
else:
    print("Senior")

temperature = 30
if temperature<0:
    print("Freezing")
elif temperature<10 and temperature>=0:
    print("Cold")
elif temperature<25 and temperature>=10:
    print("Warm")
elif temperature<35 and temperature>=25:
    print("Hot")
else:
    print("Invalid temperature")
    


