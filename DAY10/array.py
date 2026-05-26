#three types of module //.py file
#user defined module
#built in module
# third party module

#array - import - use
#numpy - install - import - use


#following 3 ways to define array in python or import

#import array as arr

#from array import array

#from array import *

# import array as arr

# ar1=arr.array('i',[2,3,4,5])
# print(ar1)
# print(type(ar1))


from array import array

ar1=array('i',[2,3,4,5])
print(ar1)
print(type(ar1))

ar1[3]=11
print(ar1)

ar1[2:5]=array('i',[2,3,4,5])
print(ar1)

del ar1[3]
print(ar1)


a=array('B',[1,3])
# convert a to float array before concatenation to match typecode 'd'
c=array('d', a)
print(c)
