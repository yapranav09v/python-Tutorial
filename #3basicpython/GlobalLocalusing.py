#Using Global and local variable
l=10 #declaring the global variable
def fun(n):   
   # l=5 #declaring the local variable
    m=8 #we can use m inside a function we cant print it outside a function
    print(n,"I heve printed n")  
    global l
    l=l+5                                        #We can use local in local only but we can use global in both local and global
    print(l,m) #printing inside the function it will print local 
    #l=l+5 if it is local we can change but we cant change global variable without using "global" as a prefix
fun("thise is me") 
print(l) #printing l out of the function it will print global