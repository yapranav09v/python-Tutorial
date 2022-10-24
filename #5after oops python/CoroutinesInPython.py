#Use of Coroutines in python
# making a corotine                          
def searcher():
    import time
    #some 4 seconds time consuming task as an example like reading book or machine learning code
    book = " Thise is book which is written by harry and pranav for programming "
    time.sleep(4)

#we can make any function corotine using following syntax
    while True:
        text = (yield)
        #Giving a condition if the text is in the book it will print respected statment
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")

#Using a corotine using following syntax
search = searcher() 
print("Search started")

#using a next method to start the search
next(search) 
search.send("Thise") #sending text that if the text is in the book or not

#using input key to search after input key is pressed
input("press any key ")                       #Note- in the first time it will take time because of sleep() then it will run fastely
search.send("harry")                       #         because of coroutine

input("press any key ")
search.send("pranav")

input("press any key ")
search.send("book")

input("press any key ")
search.send("is")                                                                  

#closing the search
search.close()                    