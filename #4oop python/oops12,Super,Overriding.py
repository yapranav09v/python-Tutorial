#Overriding a class and using super() 
#making a class A
class A:
    classvar1 = "I am in class A"

    #making a constructor
    def __init__(self):
        self.var1 = "I am inside a class A constructor"
        self.classvar1 = "Instace var in class A "
        self.special = "special"

class B(A):
    classvar1 = "I am in class B"
    
    #making a constructor
    #if anything like a constructor get override in thise class we can't use old one
    def __init__(self):
        super().__init__() #We can use super() before constructor objects to use instance(object) in both classes
        self.var1 = "I am inside a class B constructor"
        self.classvar1 = "Instace var in class B "
        super().__init__() #if we use super() after a constructor objects it will use constructor object in just class A
        print(super.classvar1) #we can also use particular object(instance) after calling super() means A class

#making a instance(object for both classes)
a = A()
b = B()

print(b.classvar1) #thise will find instance variable first either it will in class A or class B
print(b.special, b.var1, b.classvar1)