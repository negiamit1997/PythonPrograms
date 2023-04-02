num = 1234

result = 0

for i in range(len(str(num))):
    if num > 0:
        rem = num%10
        result = result + rem
        num = num//10

print(result)

