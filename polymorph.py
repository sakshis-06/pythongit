# POLYMORPHISM
'''
MEANS IMPLEMENTING SAME METHOD IN DIFFERENT WAY
We use concept pf overloading and overriding

1.Overloading
has two types :

    i.Operator overloading
    ex: '+' acts as concatenation operator for strings 'a'+'b'            op: ab
        the same + acts as addition operator for number/integers 10+20    op:30
    ex: even * is relication ,acts as repeatation symbol in data types and also acts as multiplication

    ii.Method overloading
    same function name but different arguments number

2.Overriding


'''

#operator overloading

#operator '+'
#strings-concatenation
n='10'
m=' 20'
print(n+m)
n='hello'
m='maam'
print(n," ",m)
#numbers-add
a=1
b=3
print(a+b)

#operator *
#strings
l=[10,20]
print(l*3)
#integers
a=2
b=3
print(a*b)

#method overloading
def add():    #self is needed only when we write function in a class and not outside the class
    n=10
    m=30
    res=n+m
    print("The sum is : ",res)
add()
def add(a,b):
    print("This is method with 2 parameters",a+b)
add(10,20)
def add(x,y,z):
    print("This is method with 3 parameters",x+y+z)
add(2,4,6)


#overriding
class Parent:
    a=10
    def display(self):
        print("Parent prop")
class Child(Parent):
    a=30
    def display(self):
        print("Child prop")

c= Child()
print(c.a)
c.display()
