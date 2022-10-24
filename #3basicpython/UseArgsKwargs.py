#Using args and kwargs while adding users  #apply first normal argument then args then kwargs 
#def function_name_print(a,b,c):
    #print(a,b,c)

#function_name_print("pranav","aranav","harry")
def funargs(*args,**kwargs): #you can use different names apart from args and kwargs but * and ** are compasary
   # print(args[0])  #printing first element from tuple
   for atom in args: #applying loop for printing all elements
    print(atom) #printing atom from lst
   
    #using loop to print key and value from the dictionary that passed to the kwargs and using .items to print items
    for key,value in kwargs.items(): 
        print(f"{key} is a {value}") #printing it using f string in it to pass key and value with normal argument
lst=["pranav","aranav","harry","harish"] # declaring list to store elements
kw={"Rohan":"monitor","Harry":"instructure","programar":"cordinator","shivam":"cook"} #declaring the dictionary
funargs(*lst,**kw) #calling function and passing list as a arg and dictionary as a kwargs
