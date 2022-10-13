class student:
    usn=33
    name='abc'
    branch="ise"
    def displayfunc(self):
        #self is arguments that points to itself and it is mandatory to be mentioned else error occurs
        print("This is method")


#object of a class
s = student()
print("the usn is : ",s.usn)
print("the name is : ",s.name)
print("the branch is : ",s.branch)
s.displayfunc()


class myclass:
    n=10
    z="abc"
    def myfunc(self):
        n=90
        print("this is function")
        print("local var : ",n)
        print("instance var : ",self.n)  #self works as this here- to access the variable of class and not of the method

b1 =myclass()
print(b1.n)
b1.myfunc()


#constructor in a class
#syntax :   def __init__(self)
class demo:
    def __init__(self,n1,n2):
        self.num1=n1
        self.num2=n2
    def printfunc(self):
        print("num1: ",self.num1)
        print("num2: ",self.num2)

d = demo(10,20) #constructor
d.printfunc()
d1 = demo(30,40)
d1.printfunc()



class simple:
    def add(self,a,b):
        self.n1=a
        self.n2=b
        print("sum of numbers is: ",(self.n1+self.n2))

s=simple()
s.add(10,20)
s1=simple()
s1.add(20,50)






