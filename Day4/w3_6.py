#The key difference between the tuples and lists is that while the tuples are immutable objects the lists are mutable
values= input("Input some comma-separated numbers:")
list= values.split(",")
tuple=tuple(list)
print('List : ',list)
print('Tuple : ',tuple)