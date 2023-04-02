num  = 496

result = 0
for i in range(1,num):
    if num % i == 0:
        result = result + i

if result == num:
    print("Perfect number")
else:
    print("Not a perfect number")