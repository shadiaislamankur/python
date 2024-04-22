import json

#a python object (dict):

x={
    "name":"John",
    "age" : 30,
     "city" : "New York"
}
# convert into JSON :
y = json.dumps(x)
print(y)