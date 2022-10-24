#use of class methods
class Employ:
    number_of_leaves=8 #intilizing value in class it is like global value
    
    #creating a constructor
    def __init__(self,aname,asalary,arole):
        self.name=aname 
        self.salary=asalary      # A constructore is simple means a passing a arguments(key vulue) of instace by a class(Employ) globaly 
        self.role=arole          # and creating class key value pair of instace for all instance
        
    #creating method self for rohan
    def print_details(self):
        return f"name is {self.name} salary is {self.salary} role is {self.role}"

   # #making a class method
    @classmethod
    def change_leaves(cls,newleaves):     #class method used to access only class instance variable we can access it with any class or instance
        cls.number_of_leaves = newleaves

#creating instance
harry = Employ ( " harry " , 455 , " instructor " )
rohan = Employ ( " rohan " , 456 , " student " )

harry.change_leaves(34)
print(harry.number_of_leaves)

#intializing values to instance using constructor 
print(harry.salary)
print(rohan.name)

#printing print_details function as a rohan
print(rohan.print_details())
print(harry.print_details())