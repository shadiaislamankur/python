thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist=[100,50,65,82,23]
thislist.sort()
print(thislist)


thislist=["orange","mango","kiwi","pineapple","banana"]
thislist.sort(reverse=True)
print(thislist)

thislist=[100,50,65,82,23]
thislist.sort(reverse=True)
print(thislist)


#Sort the list based on how close the number is to 50:

def myfunc(n):
    return abs(n-5)
thislist=[100,50,65,82,23]
thislist.sort(key=myfunc)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


thislist=["banana","Orange","Kiwi","cherry"]
thislist.reverse()
print(thislist)