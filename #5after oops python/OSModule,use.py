#Use of OS module os means operating system and you know what it is
#importing os module you can get more iforamtion about os module method in python documention
import os 

print("\nchecking current dirctry...")
#print(dir(os)) :- it will show how many method we can use in it
#checking a current dirctetry
print(os.getcwd())

#we can change dir using thise
#os.chdir("c://")

print("\Taking a list of all files in folder...")
#it will give list of all files in thise folder
print(os.listdir("c://")) #if we give path it will show only that path file else it will print current dir files

#it will create a new folder
#os.mkdir("new folder")

#it will make multiple directries
#os.makedirs("this/that")

#we can rename it with thise command
#os.rename("tryexepterror.py", "TryExepterror")

print("\nTaking a environment variable...")
#we can get environment variable using this
print(os.environ.get("path"))

#to joining a two path without interfering slashes 
#print(os.path.join("c://", "pranav.txt"))

print("\nPath exists or not... ")
#it will show there is any path exist or not
print(os.path.exists("c://harry"))

print("\nFile exist or not...") 
#Using this we can search that particular file or directry is exit or not 
print(os.path.isfile("OSModule,use.py"))