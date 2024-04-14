set1={"a","b","c"}
set2={1,2,3}
set3=set1.union(set2)
print(set3)

set4={"a","b","c"}
set5={1,2,3}
set6=set4|set5
print(set6)

#Join multiple sets with the union() method:
set1={"a","b","c"}
set2={1,2,3}
set3={"John","Elina"}
set4={"apple","bananas","cherry"}
myset=set1.union(set2,set3,set4)
print(myset)

myset2=set1|set2|set3|set4
print(myset2)

#Join a set with a tuple:
x={"a","b","c"}
y=(1,2,3)
z=x.union(y)
print(z)

#The update() method inserts the items in set2 into set1:

set1={"a","b","c"}
set2={1,2,3}
set1.update(set2)
print(set1)

#Join set1 and set2, but keep only the duplicates:

set1 = {"apple", "banana", "cherry"}
set2={"google","microsoft","apple"}

set3=set1.intersection(set2)
print(set3)
set4=set1&set2
print(set4)

#Keep the items that exist in both set1, and set2:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)

#Use - to join two sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)

#Use the difference_update() method to keep the items that are not present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)

#The symmetric_difference() method will keep only the elements that are NOT present in both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3=set1.symmetric_difference(set2)
print(set3)

#You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.

set1={"apple","banana","cherry"}
set2={"google","microsoft","apple"}
set3=set1^set2
print(set3)

#Use the symmetric_difference_update() method to keep the items that are not present in both sets:

set1={"apple","banana","cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)