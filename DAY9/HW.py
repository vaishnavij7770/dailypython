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

def even(n):
    return n % 2 == 0

print(even(10))   
print(even(7))

def number(n):
    if n >= 0:
        return "Positive"
    else:
        return "Negative"

print(number(5))
print(number(-3))


# 5 example programs of recursion

# sum of first n natural number

def sum(n):
    if n == 0:
        return 0
    return n + sum(n - 1)

print(sum(4))

# count from  N to 1 

def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)

countdown(5)

# reverse string

def reverse(s):
    if len(s) == 0:
        return ""
    return reverse(s[1:]) + s[0]

print(reverse("vaishu")) 

#length string

def length(s):
    if s == "":
        return 0
    return 1 + length(s[1:])

print(length("Python"))

#print seperate char

def char(s):
    if len(s) == 0:
        return
    print(s[0])
    char(s[1:])

char("vaishu")