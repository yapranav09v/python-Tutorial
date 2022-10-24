class Employ:
    number_of_leaves=8 #intilizing value in class it is like global value
    pass        #pass is used to passing a value

#creating instance
harry = Employ ()
rohan = Employ ()

#intializing values to instance
harry.name="Harry"
harry.salary=455
harry.role="Instructor"
rohan.name="Rohan"
rohan.salary=45
rohan.role="student"

#printing values of instance
print(harry.name)
print(harry.number_of_leaves) #printing global class value in any instance
print(Employ.number_of_leaves) #pritning global class value in class
#using __dict__ function to return object dictionary
print(rohan.__dict__)
rohan.number_of_leaves=9 #we can't change global value but it will store it as a instance value
print(rohan.__dict__) #by printing dict function after changing a global value by instance it will also print changed value
#changing a global class value using class
Employ.number_of_leaves=9

print(Employ.number_of_leaves) #printing changed value in class

#printing employ dictionary
print(Employ.__dict__)
