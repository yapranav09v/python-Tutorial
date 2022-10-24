#using abstract base class and abc modul
# e
#imorting a abstractmethod from abc modul 
from abc import ABC, abstractclassmethod

#making a class shape to inherite ABC
class shape(ABC):                              #Note:-we can't make objects/instance using abstract(shape) class
    @abstractclassmethod #using a abstract method to declare method as a global method for inheritade classes
    def printarea(self): #to use thise method as a perment in every class
        return 0

#making a class rectangel and inheriting shape class for global abstract method
class rectangle(shape):
    type = "Rectangle"
    sides = 4

    #making constructor for implementing length and breadth
    def __init__(self) :
        self.length = 6
        self.breadth = 7
        
    #declaring a printarea method with respect to shape class
    def printarea(self):
        return self.length * self.breadth

#maing a object for class
rect1 = rectangle()
print(rect1.printarea()) # printing area