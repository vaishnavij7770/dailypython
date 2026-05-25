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