#using a setters ,property Decoraters,and deleters
class Employee:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        #self.email = f"{fname}{lname}@gmail.com"

    def exaplain(self):
        return f" Thise employee is {self.fname} {self.lname} "
    #using a decorater @property
    #we don't want use "()" thise bracket after calling method with object
    @property
    def email(self):
        #making an if statment in property to replace none 
        if self.fname ==None or self.lname == None:
            return "Email is not set please set it using setter"
        #we are using this for not using "()" as a property return
        return f" {self.fname}{self.lname}@gamil.com"

    #using a setter decorate/method if we want change attribute or email in email function method
    #using setter to arrange defferent syntaxed attribute
    @email.setter
    def email(self, string):
        print('setting Now...')
        names = string.split("@")[0]     #thise will seperate string by @ in two and take first
        self.fname = names.split(".")[0] #thise will sepearate string by . and give thise and that
        self.lname = names.split(".")[1] #thise seperate as upper one and print .com

    #making an deletar
    @email.deleter
    def email(self):             #when we print by using a del command it will delet f and l name
        self.fname = None
        self.lname = None

harry = Employee("Harry", "Randhava")
bhavesh = Employee("Bhavesh", "chavan")

print(bhavesh.exaplain()) 

print(harry.exaplain())
#we can change only change constructor passed argument in method function
harry.fname = "pranav"
print(harry.exaplain())

#printing fuction that we used as property decorator
print(harry.email)
harry.email = "this.that@codewithharry.com"
print(harry.email)

#deleting f name and lname usign del function
del harry.email
print(harry.email) # printing email after deleting it 