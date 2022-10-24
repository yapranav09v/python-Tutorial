s=set() #declaring the empty set
print(type(s)) #printing type of s(set)
s_fron_list=set([5,4,2,1,6,3]) #declaring the set you can also add list in it
print(s_fron_list) #printing set
s.add(1) #you can add num or char in set using thise funstion
s.add(1) #it will print 1 in only one time, because sets only take unic values, its work with Sets property
s.add(2)
s.add(3)
print(s) #printing empty set after adding 1
s1=s.union({2,3,4}) #we can do union of set
print(s,s1) #after union it will print two different sets using sets union properties
s.remove(3) #it will remove 3 from set
print(s) #it will print after removing 3
# We can use Sets properties to program like disjoint set, vain digram
