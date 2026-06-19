#public

class secure:
    name="vrushali"

s=secure()
print(s.name)    

# protected
class protect:
    _girl = "trainer"
    def _girl_method(self):
        print("she is a strong girl")
        

# p=protect()
# print(p._girl)   


class authorize(protect):
    print("this is authorized")

a=authorize()
print(a._girl)  
a._girl_method()

# private

class secrete:
    __wifi=5
    print(__wifi)
    # def _init_(self):
    #     self.__wifi=3
    
    def show(self,__wifi):     
        print(__wifi)
p=secrete()
p.show(7)
# print(p.__wifi)