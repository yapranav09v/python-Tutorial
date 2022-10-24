#Opening file using Block
with open("pranav.txt") as f: #Thise is the syntax to open file using blocks
    a=f.readlines() #declaring function as read 4 words in a
    print(a) #Printing a
#There is no need to use close() when using thise method because we already using 'with'

#Opening file using old method
f=open("pranav.txt") #If we again open same or different  file using different method or traditional method it will still open 
a=f.readlines()
print(a)
f.close()