thisset={"apple","banana","cherry"}
thisset.remove("banana")
print(thisset)

thisset2={"apple", "orange", "kiwi", "banana", "cherry"}
thisset2.discard("orange")
print(thisset2)

thisset3={"apple","banana","cherry"}
x=thisset3.pop()
print(x)
print(thisset3)

#The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

