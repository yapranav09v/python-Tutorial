#Use of imports to import things fun from other file to main file
from file import a #getting a from file (if there a same value of a in different files it will create ambiguti and collusion)
import file #importing file we usualy use thise
f=file.a #declaring file.a as f to use a value of a from file
print(f) #printing f
file.myname("pranav") #myname fun is created in file that pass name and we are importing using file. fun