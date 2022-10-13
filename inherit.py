# INHERITANCE 
'''
 Types:
1.single level
2.multi level
3.hierarchical
4.multiple
'''
#single level inheritance
class parent:
    def pdisplay(self):
        print("Parent property")
        print()
class child(parent):
    def cdisplay(self):
        print("Child property")
        
c1=child()
c1.cdisplay()
c1.pdisplay()


#multi level inheritance
class gpclass:
    def gpdis(self):
        print("Grand parent property")
class parent(gpclass):
    def pdis(self):
        print("Parent property")
class child(parent):
    def cdis(self):
        print("Child property")

ob = child()
ob.gpdis()
ob.pdis()
ob.cdis()


#hierarchical inheritance
class parent:
    def pdisplay(self):
        print("parent prop")
class child1(parent):
    def c1dis(self):
        print("Child 1 prop")
class child2(parent):
    def c2dis(self):
        print("Child 2 prop")
class child3:
    def c3dis(self):
        print("Child 3 prop")

c1=child1()
c2=child2()
c3=child3()

c1.c1dis()
c1.pdisplay()

c2.c2dis()
c1.pdisplay()

c3.c3dis()
c1.pdisplay()

#multiple inheritance
class father:
    def fdis(self):
        print("Father prop")
class mother:
    def mdis(self):
        print("Mother prop")
class child(father,mother):
    def cdis(self):
        print("Child prop")

ob=child()
ob.fdis()
ob.mdis()
ob.cdis()