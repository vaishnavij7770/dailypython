#nested if

n=34

if n>0:
    print("n is positive")
    if n%2==0:
        print("n is even")
    else:
        print("n is odd")
else:
    print("n is negative")