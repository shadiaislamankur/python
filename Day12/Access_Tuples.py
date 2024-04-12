#Access Tuple Items
thistuple=("apple","banana","cherry")
print(thistuple[1])
print(thistuple[-1])

tuple2=("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tuple2[2:5])
print(tuple2[:4])
print(tuple2[2:])
print(tuple2[-4:-1])

#check exist
tuple2=("apple","banana","cherry")
if "apple" in tuple2:
    print("Yes, 'apple' id in the fruits tuple")
