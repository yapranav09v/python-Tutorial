#creating a loop using break and continue function
while(True):
    inp=int(input("Enter a number which is greater than 100:-"))
    if inp>100:
        print("Congrats!")
        break #break will stop whole loop
    else:
        print("Try again!")
        continue #it will go back to loop again untill condition is satisfies