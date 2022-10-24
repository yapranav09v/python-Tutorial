#Use of multiply inheritance
#using same class to make multiply inheritance
class employee:
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

#making a class for multiply inheritance
class player:
    number_of_games = 4

    #making a constructor
    def __init__(self, name, game):
        self.name = name
        self.game = game 

    #making a method function
    def printdetails(self):
        return f"The name is {self.name} and the game is {self.game} "
    
#passing a argument 
shubham = player ("shubham", ["cricket","kho-kho", "foot ball"])

print(shubham.printdetails())

#making another class for multiply inheritance
#taking two classes but it give privority to first class
class cool_programer(employee,player) :
    pass
#objects of employee class (ti me asach ghetal aahe)
harry = employee ( " harry " , 455 , " instructor " ) 
rohan = employee ( " rohan " , 456 , " student " )

shubham = player("shubham", ["cricketer"]) #making shubham as player object
karan = cool_programer("karan", 57930, "coolguy") #making karan as main class object but it will become employee class object

print(karan.print_details())



 