# 5 example programs return statement

def substract(a,b):
    return a-b

result=substract(5,3)
print("diffrence is:",result)


def hello():
    return "hello"

print(hello())

def square(s):
    return s*s

print(square(6))

def is_even(n):
    return n % 2 == 0

print(is_even(10))   
print(is_even(7))

def check_number(n):
    if n >= 0:
        return "Positive"
    else:
        return "Negative"

print(check_number(5))
print(check_number(-3))