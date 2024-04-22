#The nonlocal keyword is used to work with variables inside nested functions.
#The nonlocal keyword makes the variable belong to the outer function.


def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())