#use of Generators in python
"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration -

"""
#making loop for generator
def gen(n):
    for i in range(n):
        yield i   #Using yield function to make generator

#making and printing generator
g = gen(3)
print(g.__next__()) 
print(g.__next__())
print(g.__next__())

b = "harry"
ler = iter(b)
print(ler.__next__())
print(ler.__next__())
print(ler.__next__())

#for i in b:
 #   print(i)