# using try except exception function 
#for as an exception for error and run next code and also show exact error 
num1=input("Enter a first no:-")
num2=input("Enetr a sec. no:-")#declaring code
#syntax of exception function
try:   
     print("Your ans:-",char(num1)+char(num2))
except Exception as e:
     print(e) #printing e and e means error
print("Thise is very important")

#Thise thing will run first code make secound code error as an exception,show the error and then run the next code after the error
