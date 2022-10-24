#Use of raising exception in python Using raise keyword
#for more iformation about built in exception in python you can visit built in exception in python on google
a = input("Enter your name:- ")
b = input("what is your age:-")

if int(b)==0 :                             
    raise ZeroDivisionError("Ivalid age!")

if a.isnumeric():
    raise Exception("Numbers are not allowed!")

print(f" hello {a}")                                                                           
