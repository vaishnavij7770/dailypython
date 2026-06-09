def display():
    s1 = "Hello"
    yield s1
    s2 = "World"
    s3 = "Python"
    yield s2
    yield s3

display()

# for i in display():
#     print(i)


a=display()
print(next(a))  
print(next(a))
print(next(a))