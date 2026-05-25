#default function with return
a=9         #global variable

def logic():    
    a1=3    #local variable
    b1=5    #local variable
    c=a1+b1
    return c    #no need to print
    #return b1            #we cant return multiple times in a function
logic()
print(a)

#print(a1)      #wrong way to print local variable

print(logic())


add=logic()
print(add)


#parameterizd function with return

def swap(m,n):      #parameter/local variables
    temp=m
    m=n
    n=temp
    return m,n

print(swap(8,9))

result=swap(0,1)
print(result)