#Reverse a string
def rev_Str(string):
    reverse = ''
    for i in string:
        reverse =  i + reverse

    return reverse


result = rev_Str("Informatics")
print(result)