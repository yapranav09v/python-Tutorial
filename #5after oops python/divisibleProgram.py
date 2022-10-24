
def divisible():
    lst = []
    n=int(input("Enter a number:"))
    for i in range(100):
        if i%n==0 :
            lst.append(i)
    print(lst)
    c = len(lst)
    print("Total number divisible:-",c)

while(True):
    divisible()