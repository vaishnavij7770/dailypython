import os
# a=open("demo.txt","r")
# # print(a.read())
# # print(a.read(5))

# # print(a.readline())

# for i in a:    # to run all lines in one time
#     print(i)

# b=open("demo.txt","w")
# b.write("this is python date")


# c=open("demo.txt","a")
# c.write("python is prog lang")

# os.remove("demo.txt")

if os.path.exists("demo.txt"):
    os.remove("demo.txt")

else:
    print("file does not exists")

with open("demo.txt","r") as e:
    file=e.read()
    print(file)