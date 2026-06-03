try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise ValueError("You must be at least 18 years old to proceed.")
    else:
        print("Welcome! You are eligible to proceed.")

except ValueError as v:
    print(v)

    print("ValueError but program successfully executed.")

finally:
    print("Thank you for using our service.")