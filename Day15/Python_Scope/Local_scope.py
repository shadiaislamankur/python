def myfunc():
    x=300
    print(x)
myfunc()

#Function Inside Function
def myfunc2():
    x=300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()

