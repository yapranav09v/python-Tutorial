f=open("yadav.txt","w") # W stands for writting a file if file was not available it will creat one with that name
#if there is a file that have same name as ours then it will replace their content with ours
f.write("pranav bhai is a good bhai") #we can write using that function
f.close()

f=open("yadav.txt","a") # a stands for append it add content at the end of the file
f.write(" (appended)good bhai means good bhai\n") #we can write using that function
a=f.write(" (appended)good bhai means good bhai") #declaring write function as "a"
print(a) #it will show number of charecters that you write
f.close()

# Write mod means replace your charecters with our charectars and Append means add our charectars at the end of your charecters