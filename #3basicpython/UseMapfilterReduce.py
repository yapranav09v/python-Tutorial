#Use of mapfilter and reduce
#First using map
numbers = ["3","34","64"] #Declaring the list of numbers in charecters
numbers = list(map(int , numbers)) # numbers is equal to list of numbers in map function using int to covert numbers in integer
numbers[2] = numbers[2] + 1 #adding 1 in 64 from the numbers list
print(numbers[2]) #printing it

#2

num=[2,3,4,5,6,7,8,9,10] #declaring the integer list
# converting num list into a lambda function who returns square's by using a map function
square=list(map(lambda x: x*x, num)) 
print(square) #printing a square

#Using filter
#declaring the list
lst=[2,3,4,5,6,7,8,9,10]

#filtering number greter than 5 from lst using lambda fuction which returns numbers greater than 5 using fiter fun in list as gr_than_5
gr_than_5 = list(filter( lambda x:x>5,lst))
print(gr_than_5) 

#Example function
lista=[1,2,3,4]
#we want to plus 1+2 is 3 then 3+3 is 6 then 6+4 is 10
number=0 #declaring it 0 to intialize its value to zero
for item in lista:
    number=number + item #for logic adding number to item number and so on untill the results
print(number)

#Using Reduce function
#for example fuction to code same thing in one line
#importing reduce function from functools
from functools import reduce
#reducing  lista using lambda function in reduce as numbera
numbera= reduce(lambda x,y:x+y , lista)
print(numbera)
umbera= reduce(lambda x,y:x*y , lista) #Using multiplication instead of addition to reduce
print(umbera)