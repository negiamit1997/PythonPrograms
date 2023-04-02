#Armstrong number


num = 153

temp = num

n = len(str(num))

result = 0
for i in range(n+1):
    rem = temp%10
    result = result + rem**n
    temp = temp//10


if num == result:
    print("Number is armstrong")
else:
    print("Number is not armstrong")