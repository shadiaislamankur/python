def larger_string(text,n):
    result=""

    for i in range(n):
        result=result+text

    return result
    
print(larger_string('abc',2))

print(larger_string('.py',3))