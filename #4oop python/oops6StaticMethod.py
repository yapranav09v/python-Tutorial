#Use of static method 
#static method is used for a simple things
#thise is normaly we use like out of the class
class Employee:
    pass
#Creating a static method
    @staticmethod
    def sample(string):
        print("good things "+string)

#calling static method out of @staticmethod using class employee 
Employee.sample("pranav")