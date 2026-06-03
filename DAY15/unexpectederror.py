# try:
#     age = int(input("Enter your age: "))

#     if age < 18:
#         # raise ValueError("You must be at least 18 years old to proceed.")
#         raise Exception("Error")
#     else:
#         print("Welcome! You are eligible to proceed.")

# # except ValueError as v:
# #     print(v)
# except Exception as v:
#     print(v)

#     print("ValueError but program successfully executed.")

# finally:
#     print("Thank you for using our service.")


# numbers = [1, 2, 3]

# try:
#     print("Fourth element:", numbers[7])  
# except IndexError:
#     print("Error: List index out of range.")
# finally:
#     print("Execution finished for list program.")


# try:
#     value = int(input("Enter a number: "))
#     if value < 0:
#         raise ValueError("Negative numbers are not allowed.")
#     else:
#         print("You entered Positive Number:", value)

# except ValueError as v:
#     print(v)

# finally:
#     print("Execution finished ")

try:
    num=int(input("Enter a number: "))
    if num%2==0:
        print("Even number")

    else:
        raise ValueError("Odd number")

except Exception as e:
    print(e)

finally:
    print("Execution finished")