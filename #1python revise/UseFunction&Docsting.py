#use of function and docstring
a=5
b=8
print(sum((a,b))) #sum is built in function

#Syntax of Function
def fun1(a,b):  #defying the function1  and declaring the variable
    print("Your in function",a+b) #giving as a sum of variable
def fun2(a,b): #defyining function2 and passing variables
    """Thise is a function which will calculate average of two numbers""" #declaring the Docstring for info of function
    average=a+b/2 #declaring average 
    print(average) #printing average it will return value after calling function
    return average  #Returning average it will return average without calling a function

fun1(5,7) #calling function1 and giving its sum and also passing values for the sum
v=fun2(5,8) #declaring fun2 as a v : it will only used after return function
print(v) #it will give average twice #1:when fun2 is called,#2:it will declared and printed as a "v" after declaring return average
print(fun2.__doc__) #calling a function using docstring for info of function

print(sum.__doc__)#thise is showing inbuilt function info
