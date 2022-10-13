# ABSTRACTION
#CONCRETE CLASS IS DERIVED CLASS OF THE ABSTRACT CLASS
'''
#we cannot create object for an abstract class
the abstract class has only the declaration part of the functions where as 
concrete class has the definition of that class which is declared
#abstract class has abstract methods which are only declared and not defined 
#ABC is an abstract class ,it is built in
# here @ is called as decorator
'''
from abc import ABC, abstractmethod
#abstract class
#we cannot create object for an abstract class
class Abdemo(ABC):
    #creating a abstract method
    @abstractmethod
    def abmethod(self):
        None  # here we are declaring it so just write "None"
#creating a concrete class
class Concretedemo(Abdemo):
    def abmethod(self):
        print("This is abstract function ")
ob=Concretedemo()
ob.abmethod()
