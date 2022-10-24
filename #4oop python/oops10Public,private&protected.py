#use of public private and protected Access Specifires
class employee:
    number_of_leaves=8 #this is public variable
    #Creating a protected variable using a underline("_")
    #we can use thise variable in our own class and class that made up with thise class or inheritance class
    _protected = 5  

    #making a private variable using double underscore ("__")
    #we can only use private variable in our thise class we can't use it outside the class
    __private = 6
    
    #creating a constructor
    def __init__(self,aname,asalary,arole):
        self.name=aname 
        self.salary=asalary      
        self.role=arole         
        
    #creating method self for rohan
    def print_details(self):
        return f"name is {self.name} salary is {self.salary} role is {self.role}"

    ##making a class method as constructor alternative
    @classmethod
    def from_str(cls , string):     #passing a cls as class and string
        paras = string.split("-")   #using split function to split string
        return cls(paras[0], paras[1], paras[2])    #returning splited string as a list in cls(class method_constructor)
        #doing same thing from above function in one line using *args
        return cls(*string.split("-"))

pro = employee("pro", 543, "emo")  #Crating a new instancer or object to print protected no.
#printing a protected variable
print(pro._protected)

#Printing a private class
#because of python namemagline we have to use underscore"_" and class name like _employee
print(pro._employee__private)
