# try:
#     a=int(input("Enter 1st number:"))
#     b=int(input("Enter 2nd Number:"))


#     c=a/b       #4/0
#     print(c)    #exception handle
# except:
#     print("Something went wrong")
#     print("Please check your input and try again")

#     print("program executed successfully")




try:
    a=int(input("Enter 1st number:"))
    b=int(input("Enter 2nd Number:"))


    c=a/b       #4/0
    print(c)    #exception handle

except NameError as n:
    print(n)

except IndentationError as i:
    print(i)

except ZeroDivisionError as z:
    print(z)

except Exception as e:

    print(e)

finally:
    print("program executed successfully")