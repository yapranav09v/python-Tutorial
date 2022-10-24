#Using a list Comprehensions
#making a example from simple method
lst = []
for i in range(100):
    if i%3==0 :
        lst.append(i)
print(lst)

#Now using list Comprehension method
print("\nlist Comprehensions")
ls = [i for i in range(100) if i%3==0]
print(ls)
print() 

#Now using dictionary Comprehansions
print("dictionary Comprehensions")
dict1 = {i:f"item{i}" for i in range(11)}
print(dict1)
print()

#Now using set Comprehensions
print("set Comprehensions")
dresses = {dress for dress in["dress1", "dress2","dress1", "dress2","dress1", "dress2"]}
print(dresses)
print(type(dresses))
print()

#Generator Comprehensions
print("Generator Comprehensions")
events = (j for j in range(100) if j%2==0)
print(events.__next__())
print(events.__next__())
print(events.__next__())
print(events.__next__())
print(type(events))

