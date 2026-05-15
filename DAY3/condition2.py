#nested if

n=34

if n>0:
    print("n is positive")
    if n%2==0:
        print("n is even")
    else:
        print("n is odd")
else:
    print("n is negative or zero")

age = int(input("Enter age: "))

if age >= 18:
    if age >= 60:
        print("Senior Citizen")
    else:
        print("Adult")
else:
    print("Minor")

password = input("Enter password: ")

if len(password) >= 8:
    if password== "password123":
        print("Password is correct")
    else:
        print("Password is incorrect")
else:
    print("Password is too short")

marks=78
if marks>=90:
    if marks==100:
        print("Grade: A+")
    else:
        print("Grade: A")
else:
    print("Grade: B or below")
