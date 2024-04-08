number1=20
number2=30
Roll=10
username="Ankur"
print("This is my super number" ,number1+number2)
print(f"This is my super number {number1+number2}")
print(f"My name is {username} & my classrole is {10}")


#Byte type data
_list=[1,2,3,4,5,6,7,8]
b=_list
b=bytes(_list)
print(type(b))

#bynary type data byteArray
_list2=[1,2,3,4,5,6,7,8,255]
b2=bytearray(_list2)
b2[1]=10

print(b2[1])
print(_list2)

