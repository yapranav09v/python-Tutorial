#using a pickle module
#importing a pickle module
from operator import length_hint
import pickle

#pickling a python object
cars = ["Audi", "maruti suzuki", "harryti Tuzuki", "lamborgini"]

file = "mycar.pkl"
fileobj = open(file, 'wb') #making/writting file in binary
pickle.dump(cars, fileobj) #dump takes arguments object and file object not a file
fileobj.close() #closing the file

file = "mycar.pkl"
fileobj = open(file, 'rb') #openig/reading file in binary
mycar = pickle.load(fileobj) #load will take file obj and return it 
print(mycar)
print(type(mycar)) 