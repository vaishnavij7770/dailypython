result= lambda a,b:a+b
res=result(7,8)
print(res)


square = lambda s:s*s
squ=square(6)
print(squ)

cube = lambda n:n*n*n
num=cube(8)
print(num)

maximum = lambda x, y: x if x > y else y
n=maximum(10, 15)
print(n)

even_odd= lambda e:e%2==0
print(even_odd(2))

#check divisible by 5

divisible= lambda f:f%5==0
print(divisible(23))