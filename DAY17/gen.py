def logic():
    for i in range(1, 11):
        yield i

logic()


for i in logic():
    print(i)