#When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

fruits= ("apple","banana","cherry")
#unpacked
(green,yellow,red)=fruits

print(green)
print(yellow)
print(red)

#using asterisk*
fruits2=("apple", "banana", "cherry", "strawberry", "raspberry")
(green,yellow,*red)=fruits2
print(green)
print(yellow)
print(red)