#Use of continue and break
i=0
while(True): #declaring while True its endless loop
    if i+1<5:
        i=i+1
        continue #continue function in that if condition not satisfies it will go back to loop again and after matching the the condition it will run futher condition
    print(i+1, end=" ")
    if i==99:
        break #break will stop the loop after condition satisfies and also go back to continue
    print("You printed no. untill hundred")
    i=i+1