"""
15
14 13
12 11 10
9  8  7   6
5  4  3   2  1
"""
n = int(input("Enter no of rows:\n"))
k=0
for i in range(n+1):
    k = k+i

for row in range(1,6):
    for col in range(row):
        print(k, end="")
        k=k-1
    print()


