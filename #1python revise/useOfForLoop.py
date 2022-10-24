#Use of loops
list1=["harry","larry","carry","marry"] #declaring the list
#For loop Syntax
for item in list1: #for loop declaration for list 
    print(item)

list2=['ew','re','ty',3,1,6,'ty',8,9,'ui',10,'sar'] #declaring the mixed list
for item in list2: 
    if str(item).isnumeric() and item>=6: #giving if condition and using isnumeric() function, giving str because theire is str in list
        print(item)
        
    