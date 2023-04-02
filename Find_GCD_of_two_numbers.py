#Find GCD(greatest common divisor) of two numbers  OR  HCF (Highest common factor)
#Euclids
"""
def gcd_number(a,b):
    if b ==0:
        return a
    else:
        return gcd_number(b,a%b)

r1 = gcd_number(12,18)
print(r1)
"""


#gcd of two numbers

x = int(input("Enter 1st number:\n"))
y = int(input("Enter 2nd number:\n"))

if x > y:
    x,y = y,x

gcd = 0
for i in range(1, x+1):
    if x%i==0 and y%i==0:
        gcd = i

print(f"gcd of {x} and {y} is {gcd}")


