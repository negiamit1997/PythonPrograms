n= int(input("Enter the number you want in fabonacci series:\n"))

first = 0
second = 1
print(first, second, end = ' ')
for i in range(n+1):
   result = first + second
   print(result, end = ' ')
   first = second
   second = result

