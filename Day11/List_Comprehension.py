fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[]

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

#with one line code

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
mewlist=[x for x in fruits if "a" in x]
print(newlist)

#The condition is like a filter that only accepts the items that valuate to True.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist=[x for x in fruits if x!= "apple"]
print(newlist)

#With no if statement:

newlist =[x for x in fruits]
print(newlist)

#Iterable
#The iterable can be any iterable object, like a list, tuple, set etc.

newlist = [x for x in range(10)]
print(newlist)

#Accept only numbers lower than 5:
newlist=[x for x in range(10) if x<5]
print(newlist)

newlist=[x.upper() for x in fruits]
print(newlist)

#Set all values in the new list to 'hello':
newlist =["hello" for x in fruits]
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)