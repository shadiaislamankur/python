def my_function():
    print("Hello from a function")
my_function()


def my_function(fname):
    print(fname+" Refsnes ")
my_function("Email")
my_function("Tobias")
my_function("Linus")


def my_function(fname,lname):
    print(fname+" "+lname)
my_function("Email","Refsnes")


def my_function(*kids):
    print("The youngest child is "+ kids[2])
my_function("Email","Toboas","Linus")


def my_function2(child3,child2,child1):
    print("The youngest child is "+child3)

my_function2(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

def my_function(**kid):
    print("His last name is "+kid["lname"])
my_function(fname = "Toboas", lname="Refsnes")


def my_function4(country="Norway"):
    print("I am from "+country)
my_function4("Sweden")
my_function4("India")
my_function4()
my_function4("Brazil")


def my_function(food):
    for x in food:
        print(x)
fruits=["apple","banana","cherry"]
my_function(fruits)


def my_function(x):
    return 5*x
print(my_function(3))
print(my_function(5))
print(my_function(9))

def myfunction():
    pass

print("-----------------------------------------")
def my_function(x,/):
    print(x)
my_function(3)

print("-----------------------------------------")

def my_function(*,x):
    print(x)
my_function(x=3)

print("-----------------------------------------")
def my_function(a,b,/,*,c,d):
    print(a+b+c+d)
my_function(5,6,c=7,d=8)


print("-----------------------------------------")
def tri_recursion(k):
    if(k>0):
        result=k+tri_recursion(k-1)
        print(result)
    else:
        result=0
    return result
print("\n\nRecursion Example Results")
tri_recursion(6)

print("-----------------------------------------")

x=lambda a:a+10
print(x(5))

print("-----------------------------------------")

x=lambda a,b:a*b
print(x(5,6))

print("-----------------------------------------")
x=lambda a,b,c : a+b+c
print(x(5,6,2))

print("-----------------------------------------")

def myfunc(n):
    return lambda a:a*n
print("-----------------------------------------")

def myfunc(n):
    return lambda a:a*n
mydoubler=myfunc(2)
print(mydoubler(11))

print("-----------------------------------------")

def myfunc(n):
    return lambda a:a*n
mydoubler=myfunc(2)
mytripler=myfunc(3)

print(mydoubler(11))
print(mytripler(11))