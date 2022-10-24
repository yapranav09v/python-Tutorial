def printhar(str): #declaring a function to pass a string
    return f"your name is {str}"

# declaring a function to add two numbers
def add(num1, num2):
    return num1+num2+9

#declaring name equals main function to not get into a  another imported file
if __name__ == '__main__':
    a=add(5,3)
    print(a)
    print(5*a)