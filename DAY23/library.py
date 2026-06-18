import numpy as np

arr=np.array([1,2,3,4,5])
print(arr)

print(type(arr))

arr1=np.arange(1,11)
print(arr1)

arr2=np.ones(10)
print(arr2)

arr3=np.zeros(10)
print(arr3)

#0D array
a1=np.array(50)
print(a1)

#1D array
a2=np.array([4,5,6])
print(a2)

#2D array
a3=np.array([[5,5,5],[6,6,6]])
print(a3)

#3D array
a4=np.array([[[1,2],[1,2]],[[1,2],[1,2]]])
print(a4)


a5=np.array([10,2,3,4,5,6,7,8,9,4,5,6])
a6=np.where(a5%2==0)

print(a6)

a7=np.sort(a5)

print(a7)

a8=a5.reshape(3,4)
print(a8)

a9=a5.reshape(2,3,2)
print(a9)

a10=np.array([[5,5,5],[6,6,6]])
for i in a10:
    for j in i:
        print(j,end=" ")