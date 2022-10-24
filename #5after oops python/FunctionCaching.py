#Using function caching
#function caching is used to store proccesed information and use that in next same process to run it faster in zero time
import time  #usign time module for creating delay
from functools import lru_cache #thise is used to store cache

#declaring the cache function and its size for store cach information in some work function 
@lru_cache(maxsize=3)
def some_work(n):
    #some task taking n secounds
    time.sleep(n)
    return n

#declaring a main function to call a some_work function
if __name__ == '__main__':
    print("Now running some work")
    some_work(3)                  #it will delay only for thise function becaus of cache
    print("Done...Calling again")          #Creating delay and print after dalay
    some_work(3)           #it will run quickly
    print("called again")
    some_work(3)           #it will run quickly
    print("called again")
    some_work(3)           #it will run quickly
    print("called again")