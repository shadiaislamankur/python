thislist=["apple","banana","cherry"]
for x in thislist:
    print(x)

print("-------------------------------------")

#Print all items by referring to their index number:

thislist=["apple","banana","cherry"]
for i in range (len(thislist)):
    print(thislist[i])


#Print all items, using a while loop to go through all the index numbers
print("-------------------------------------")

thislist=["apple","banana","cherry"]
i=0
while i<len(thislist):
    print(thislist[i])
    i+=1

print("-------------------------------------")
thislist =["apple","banana","cherry"]
[print(x) for x in thislist]

