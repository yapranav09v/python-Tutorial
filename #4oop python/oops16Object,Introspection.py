#Object introspection means fining type(type of any object),id(finding object id in numbers),dir(finding number of methods and function on that particular object)
#making a class for using introspection
class Introduction:

    def __init__(self, fname, lname, lage):
        self.fname = fname
        self.lname = lname
        self.lage = lage

    def name(self):
        return f"The name is {self.fname} and last name is {self.lname} and he's age is {self . lage}"

rohan = Introduction("Rohan", "sharma", 18)

print(rohan.name())


#Using Introspection
print(type(rohan))
print(id(rohan))
print(dir(rohan))

#Using inspect module
import inspect

#print(inspect.getmembers(rohan))
