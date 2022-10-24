#Read and Write file both using "r+" 
f=open("RD.txt", "r+") #r+ is used for read and write both in exiting file
f.write("read and write file\n")
print(f.read())
f.write("thank you")
print(f.read())
f.close()
 
