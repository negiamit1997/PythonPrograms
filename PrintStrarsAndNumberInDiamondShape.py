"""
     * 1
    ** 23
   *** 345
  **** 4567
 ***** 56789
****** 67891011
654321 1357911
 65432 357911
  6543 57911
   654 7911
    65 911
     6 11
"""
Z=1

for i in range(0,6):
    m= i+1

    for j in range(5,i,-1):
        print(" ", end="")
    for k in range(i+1):
        print("*", end="")
    print(end = " ")
    for l in range(0,i+1):
        print(m, end="")
        m = m+1
    print()

for n in range(6):
    for c in range(n):
        print(" ", end="")
    for b in range(6,n,-1):
        print(b, end="")

    print(end=" ")

    Q = Z
    for x in range(6,n,-1):
        print(Q, end="")
        Q = Q + 2

    Z = Z + 2
    print()



