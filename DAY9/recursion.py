# recursion - condition 100 times

#4!=4*3*2*1
#n!=n*(n-1)!

#1!=1
#0!=1

def facto(n):
    if n<=1:
        return 1
    else:
        return n*facto(n-1)
    
print(facto(5))


def fact(m):
    if m<=1:
        return 1
    else:
        return m*fact(m-1)
n=int(input("Enter a number:"))

print(fact(n))

