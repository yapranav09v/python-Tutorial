#Using a special methods like operator,Overloading, Dundler
class employee:
    number_of_leaves=8 
    
    #creating a constructor
    #It is a kind of dunder method a special method
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

    #This is a Dunder method a special method it is helpign in operator overloding 
    #making an method to add salary from emp1 and emp2 in employee
    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary  #Note:-#For more information you can search mapping operators to function in python

    #making a method that can return print_details of any instance printed 
    #using a special method
    def __repr__(self):
        return self.print_details()

#making objects(instance)
emp1 = employee("Harry",78,"programer")
emp2 = employee("Rohan",56,"compounder")

print(emp1 + emp2)
print(emp1 / emp2)

print(emp1)