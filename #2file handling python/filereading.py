#Using file writting
open("pranav.txt","r") #used for opening the file
# making a file pointer to use a file
f=open("pranav.txt") #declaring open file as a f
content=f.read(500) #declaring content is equal to f(file) and read() used to read the file f.read() you can also give a number that how many letter you want to type
print("1",content) #printing content as a file

f.close() #used to closing the file
