d={11:111,12:112,13:113,14:114,15:115}
print(d)
print(type(d))
print(d[13])

d1=dict({"name":"vaishu", "qualification":"b.tech", "city":"satara", "gender":"female","age":"22"})
print("I am",d1["name"])
print("i am living in",d1["city"])

d2=d1.get("city")
print(d2)

d3=d1.copy()
print(d3)

d1.pop("gender")
print(d1)

d1.items()
print(d1)

print(sorted(d1.keys()))
print(sorted(d1.items()))

d1.update({"age":"22","id":"1"})
print(d1)

d1.popitem()
print(d1)