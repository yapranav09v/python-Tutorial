#Indroduction to oops
#Creating a class
class student:
    pass
harry =student()  #creating a two instance for class
larry =student()

harry.name="pranav" 
harry.stdd=12
harry.age=18       #initializing values and char and also a list in instance          
larry.name="larry"      
larry.std=11
larry.subjects=["hindi","marathi","physics","chemistry","physics"]
print(harry.name,harry.stdd)  #priting instace with respect to its value
print(larry.name,larry.std)
print(harry.name,larry.subjects)