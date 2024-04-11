mylist=["apple","banana","cherry"]
print(mylist)

#Allow duplicates
mylist=["apple","banana","cherry","apple","cherry"]
print(mylist)

#List Item - Data Type
list1=["apple","banana","cherry"]
list2=[1,2,3,4,5]
list3=[True,False,False,True]

#A list with strings, integers and boolean values:

list4=["abc",34,True,"female"]
print(list4)

print(type(list4))

#list can be modified . It is mutable
li=[2,98,9,0]
li[1]=10
print(li[1])
print(li)
print(li[-1])

#Return third fourth fifth item:
thislist=["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])

if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

#changing Item Value

thislist=["apple","banana","cherry"]
thislist="lichi"
print(thislist)

#Change a Range of Item Values
thislist=["apple","banana","cherry","orange","kiwi","melon","mango"]
thislist[1:3]=["blackcurrant","watermelon"]
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#inserthing Items
thislist=["apple","banana","cherry"]
thislist.insert(2,"watermelon")
print(thislist)

#adding items using append()
thislist=["apple","banana","cherry"]
thislist.append("orange")
print(thislist)

thislist=["Gwava","apple","banana","cherry"]
print(thislist.insert(1,"orange"))

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Add elements of a tuple to a list:

thislist=["apple","banana","cherry"]
thistuple=("kiwi","orange")
print(thislist)