#default function

def hello():
    print("hello this is mansoon")

hello()

def add():
    a=4
    b=6
    print(a+b)
add()

#parametrized function

def abc(phrase):
    print(phrase)

    phrase1="already reached"
    print(phrase1)


abc("mansoon coming")

# required argument
def operate(m,n):          #parameter 
    o=m*n
    print("multiplication=",o)

operate(7,5)        #arguments

#keyword argument

def bio(id,name,age):
    print(id)
    print(name)
    print(age)

bio(name="python",id=101,age=46)

#default arguments

def display(area,city,state="Mah"):
    print(area,city,state)

display("snagar","pune","HP")

#variable length arguments

def show(name,*marks):              #arguments  //tuple
    print(name)
    print(marks)

show("python",78,67,89,45,45)

def show1(name,**marks):              #arguments  //dict
    print(name)
    print(marks)

show1("python",M=78,C=67,G=89,B=45,S=45)



