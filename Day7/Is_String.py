def new_string(text):
    if len(text) >=2 and text[:2] == "Is":
       return text
    
    else:
        return "Is"+text
    
print(new_string("Array"))
print(new_string("IsEmpty"))
    