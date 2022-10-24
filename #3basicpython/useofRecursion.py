#Use of recursion to calculater a factorial
def fact(n):   #defining a function and passing variable n
    if (n==0 or n==1):  #condition for fact to non 0 and 1
        return 1 #if condition satisfies returning 1
    else:
        return n*fact(n-1) #else condition to be working of fact formula  3*2!
num = int(input("Enter a number:- "))                          #          2*1!
if(num<0):                                                     #          return 1 then calculater all no. and giving output
    print("factorial doesn't exist!") #if number is negative then factorial doesn't exist
else:
    print("Factorial of number is:- ", fact(num)) # |Calling fact function and passing value of sum to the n