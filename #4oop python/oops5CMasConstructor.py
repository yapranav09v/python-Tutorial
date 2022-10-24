#use of class methods as a alternative constructor
class method_constructor:
    number_of_leaves=8 
    
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
#creating instance
harry = method_constructor ( " harry " , 455 , " instructor " )
rohan = method_constructor ( " rohan " , 456 , " student " )
karan = method_constructor.from_str("karan-480-student")  #making another object(instance) and using class method(from_str) for rearrange it

print(harry.number_of_leaves)
print(karan.print_details())
