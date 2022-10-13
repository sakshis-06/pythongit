# ENCAPSULATION
# using access specifiers such as public(default) and private

#public class of encap
class Sample:
    a=1   # this is public instance variable
    def displayencap(self):
        print("This is encapsulation function")

ob = Sample()
print(ob.a)
ob.displayencap()

#private class of encap
class Sample:
    __a=1   #this is private instance variable
    def displayencap(self):
        print("The private varibale value is : ",self.__a)
        print("This is encapsulation function")
        

ob = Sample()
ob.displayencap()


#simple example
class b:
    __a=1000
    def p(self):
        print(self.__a)
ob = b()
ob.p()

