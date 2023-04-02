from math import gcd

num = int(input("Enter the number:\n"))

lower = int(input("Enter lower limit:\n"))
upper = int(input("Enter upper limit:\n"))


for i in range(lower, upper+1):
    if gcd(num,i) == 1:
        print(i)




