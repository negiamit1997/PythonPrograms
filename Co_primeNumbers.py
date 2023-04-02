#when gcd of two numbers are 1 then numbers are called co-prime
"""
num1 = int(input("Enter num1:\n"))
num2 = int(input("Enter num2:\n"))


if num2>num1:
    num1, num2 = num2, num1


expected_gcd = 1

gcd = 0
for i in range(1, num1+1):
    if num1%i==0 and num2%i==0:
        gcd = i

print(gcd)
if expected_gcd == gcd:
    print("Numbers are co-prime")
else:
    print("Numbers are not co-prime")"""
from math import gcd

num1 = int(input("Enter num1:\n"))
num2 = int(input("Enter num2:\n"))

if gcd(num1, num2) ==1:
    print(f'{num1} and {num2} are co-prime')
else:
    print(f'{num1} and {num2} are not co-prime')