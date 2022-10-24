#Use of enumerate function

#First using a traditional method
lst=["aloo","bhindi","chovmin","chicken"]
i=1 #declaring it for index no. of item 
for item in lst:
    if i%2!=0: #giving condition to print second atom in lst because it's idex starts with a 1
        print(f"jarvis please by {item}")
    i+=1 #incrementing index by 1

    #Now using a enumerate function 
for index,item in enumerate(lst):   #index is used to index no. of item using enumerate in lst
    if index%2==0:  #using thise condition because it's index starts with 0 and we want a second item
        print(f"jarvis please by a {item}") 