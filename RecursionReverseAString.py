#Reverse a string using recursion

str = "Rudreshwar"

def func1(new_str):
    if len(new_str) == 1:
        return new_str
    else:
        return func1(new_str[1:]) + new_str[0]


str2 = func1(str)
print(str2)