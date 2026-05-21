set1=set([1,3,5,2,4,6,8])
print(set1)

set2={1,3,5,7,'s'}
print(set2)

set2.add(29)
print(set2)

set2.remove(1)
print(set2)

set2.pop()
print(set2)

set2.discard('s')
print(set2)

set2.update(set1)
print(set2)

set2.union(set1)
print(set2)

set3=set2.intersection(set1)
print(set3)

set4=set2.difference(set1)
print(set4)


print(set1.issubset(set2))


# set5={"a","c","e"}
# set6={"b","e","d"}
# set7={"a","r","s"}

# set5.intersection_update(set6,set7)
# print(set5)


set5={"a","c","e"}
set6={"b","e","d"}


set9=set5.symmetric_difference(set6)
print(set9)