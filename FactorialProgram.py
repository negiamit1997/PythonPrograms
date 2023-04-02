#Factorial of a number
num = 5
result = 1;
for i in range(num,0,-1):
    result = result * i

print(result)



#Facrtorial of a number by recursion

def fac_num(num):
    if num == 0:
        return 1
    else:
        return num * fac_num(num-1)



n1 = fac_num(6)
print(n1)