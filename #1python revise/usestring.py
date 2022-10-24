                        #string data type
mystr='harry is a good boy' #declaring the string
print(mystr) #printing the string
print(mystr[4]) #slicing the string and printing 'a' character
print(mystr[0:5]) #slicing the string string to print 0 to 5 char
print(len(mystr)) #printig a length of string
print(mystr[0:78]) #slicing and printing maximum string if only [78] is given then it will give error if you give [0:78] it will print
                    #  0 to where there rang is.
 
#Advance slicing
print(mystr[0:10:2]) #in adavance slicing 0:10 print 10 charecters and skip one charecter from start and print 
print(mystr[::]) #if we put it empty like that then first colmun is "0" secound is "19"(lenght of string) and last one is "1" it skips nothing
#Negative index
print(mystr[0:-5]) #it wil skip last 5 letters
print(mystr[-6:]) #it will print reverse from last to 6 from last
print(mystr[::-1]) #THISE is a kind way to reverse a string __#1column 0, #2column 19(size of string), #3column starts it from back ans skip no char
#Some function in string
print(type(mystr)) #it can tell type
print(mystr.endswith("boy")) #to see its ending charecter
print(mystr.count("o")) #0to count char in string
print(mystr.find("is")) #to find char in string
print(mystr.upper()) #to convert string into upper capital
print(mystr.lower()) #to convert string into lower small
print(mystr.replace("harry","pranav")) #to replace a string
#for more you can search "python string function" 
