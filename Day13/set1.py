myset={"apple","banana","cherry"}
print(myset)

#duplicates not allowed here
thisset={"apple", "banana", "cherry", "apple"}
print(thisset)

#True and 1 is considered the same value:
thisset3={"apple", "banana", "cherry", True, 1, 2}
print(thisset3)

#False and 0 is considered the same value:
thisset4={"apple","banana","cherry",False,True,0}
print(thisset4)

#To determine how many items a set has, use the len() function.
thisset5={"apple","banana","cherry"}
print(len(thisset5))

#String, int and boolean data types:
set1={"apple","banana","cherry"}
set2={1,2,3,4,5,9,7}
set3={True,True,False,False}

#A set can contain different data types:
set4={"abc",34,True,40,"male"}
print(type(set4))

#It is also possible to use the set() constructor to make a set.

thisset5=set(("apple","banana","cherry")) # note the double round-brackets
print(thisset5)