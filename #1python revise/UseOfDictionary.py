#Use of dictionary
dic={"maharastrian":"marathi","gujarat":"kacchi","karnatak":"kannad","punjab":"punjabi","tamilanadu":"tamil","asam":"asami",
"India":{"hindu":"hindi","muslim":"urdu","christan":"eglish"}} #declaring the dictionary and there is a dictionary in dictionary eg. India
dic2={ }
print(dic["karnatak"]) #printing and finding key value in dictionary
print(dic["India"]) #printing and finding key value in dictionary but it shows another dictionary
print(dic["India"]["hindu"]) 
dic["bangal"]="bangali" #adding element in dictionary
dic["rajastani"]="rajput"
print(dic) #printing whole dictionary to see added element adds or not
del dic["rajastani"] #used to delet element in dictionary
print(dic) #printed to see element deleted or not
dic3=dic.copy() #used to copy dictionary one to another
dic2.update({"com":"ssam"}) #used to add element in valid way
print(dic2)
print(dic.keys()) #keys() used for printing keys the main word
print(dic.items()) #items() used for printing items the meaning of main word
#For you can search dictionary functions python                        
