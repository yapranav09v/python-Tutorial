a=int(input("Enter a no.:-")) #taking input in a
b=int(input("Enter a second no.:-")) #taking input in b
#If Else syntax(if else ladder)
if a+b<9:
    print("Its under luck") #first if and its condition
elif a+b==9:
    print("Its a luck") #elif only check one elif after the condition satisfice it will ignore all other elif
if a+b==0:
    print("unknown") #secound if it will check all if its even the condition satisfies
else:
    print("Its above luck") #last one is always else we cannot give it condition
#we can also use 'in','in not','and' in condition and 'or' many more etc.