x=("apple","banana","cherry")
y=list(x)
y[1]="kiwi"
x=tuple(y)
print(x)

#Add items
thistuple=("apple","banana","cherry")
y=list(thistuple)
y.append("orange")
x=tuple(y)
print(x)

#add tuple to tuple
thistuple2=("apple", "banana", "cherry")
y=("orange",)
thistuple2+=y
print(thistuple2)

#Convert the tuple into a list, remove "apple", and convert it back into a tuple:

thistuple3=("apple","banana","cherry")
y=list(thistuple3)
y.remove("apple")
thistuple3=tuple(y)

thistuple4=("apple","banana","cherry")
del thistuple4
print(thistuple4) #this will raise an error because the tuple no longer exists

