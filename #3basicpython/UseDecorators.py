#Use of decorators in python
def function1():
    print("pranav yadav")

fun2=function1 #declaring fun2 as a function1
del function1 #deleting function1
fun2() #caling fun2

#2
# Decorating function is nothing but using a function as a argument to change a function without changing a origanal fuction
#making a decorative function
def dec1(func1): # passing value as a fuction
    def nowexec(): #creating nested fuction
        print("\nexicuting now")
        func1 ()   #calling variable passed function
        print("exucuted")
    return nowexec #returning function values itself

#creating a decorative fuction for dec1
def who_is_pranav():
    print("pranav is a good boy")

#declaring who_is_pranav function as dec1 and passign value function as who_is_pranav function
who_is_pranav = dec1(who_is_pranav)
who_is_pranav() 

#Now using real decorative method
#using #2 fuction using decorative method

def dec2(func2): # passing value as a fuction
    def nowexece(): #creating nested fuction
        print("\nexicuting now")
        func2 ()   #calling variable passed function
        print("exucuted")
    return nowexece #returning function values itself

#creating a decorative fuction for dec2 using @(at the rate argument)
@dec2 
def who_is_pranava():
    print("pranava is a good boy")
who_is_pranava()
