# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
#     print("Result:", result)
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero!")


# try:
#     num = int(input("Enter an integer: "))
#     print("You entered:", num)
# except ValueError:
#     print("Error: Invalid input, please enter an integer.")


# try:
#     f = open("sample.txt", "r")
#     print(f.read())
# except FileNotFoundError:
#     print("Error: File not found.")

# try:
#     num = [1, 2, 3]
#     print(num[5])
# except IndexError:
#     print("Error: Index out of range.")

# try:
#     d = {"name": "Vaishnavi"}
#     print(d["age"])
# except KeyError:
#     print("Error: Key not found in dictionary.")

# try:
#     result = "hello" + 5
#     print(result)
# except TypeError:
#     print("Error: Cannot add string and integer.")


# try:
#     num = int("abc")
#     print(num)
# except ValueError:
#     print("Error: Cannot convert string to integer.")

# try:
#     import non_existent_module
# except ImportError:
#     print("Error: Module not found.")

# try:
#     x = 10
#     x.append(5)
# except AttributeError:
#     print("Error: Integer object has no attribute 'append'.")

try:
    num = float(input("Enter a decimal number: "))
    print("You entered:", num)
except ValueError:
    print("Error: Invalid input, please enter a decimal number.")
