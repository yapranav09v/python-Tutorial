#Use of join function
#declaring the list
lst = ["join","cena","randy","orton","khali"] 

#using loop to print item in list with 'and' in the middle and end=" " for not giving a new line charectar offcource
for item in lst:
    print(f" {item} and", end=" ")

#Now using 'join' function to join and in list
a=" and ".join(lst)  #a for declaring "and" to use join for adding 'and' in lst
print(a) #prining a

print ("other wwe stars") #printing extra line ASACH
