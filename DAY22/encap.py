#public
class secure:
    name="Vrush"

s=secure()
print(s.name)

#Protected
#protected is also similar like public
class more_secure:
    _profile="Trainer"  #internal

m=more_secure()
print(m._profile)

class authorize(more_secure):
    print("This is authorize")

a=authorize()
print(a._profile)

#private

class fortune:
    __wifi=5
    print(__wifi)

    def show(self,__wifi):
        print(__wifi)

f=fortune()
f.show(6)
# print(f.__wifi)

# class cravita(fortune):
#     pass

# c=cravita()
# print(c.__wifi) #not printing directly