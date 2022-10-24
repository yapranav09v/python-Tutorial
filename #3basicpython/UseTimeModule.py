import time #importing the time module
intial=time.time() #declaring intial as time() tic function in time module
#declaring the while loop
k=0
while(k<5):
    print("thise is pranav")
    time.sleep(2) #delaying the time in seconds using sleep function in time
    k+=1
print("time taken by while loop:",time.time()-intial) #printig time taken by value loop by substracting time() minus intial
intial2=time.time() #declaring another intial
for i in range(4): #declaring for loop
    print("thise is  pranav")
print("time taken by for loop:",time.time()-intial2) #same process as before but there is a intial2
#printng current time
localtime=time.asctime(time.localtime(time.time()))    #In that line (time.time()) gives ticks (time.localtime(time.time())) gives time in tuple
print(localtime)                                       # and time.asctime(time.localtime(time.time())) gives exate local time