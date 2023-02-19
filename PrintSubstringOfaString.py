#Print sub strings of a string
"""
Ex1:- string = abcd
output =
 a ab abc abcd
  b bc bcd
   c cd
    d
"""



str = input("Enter a String:\n")

for i in range(len(str)):
    for j in range(len(str)):
        print(str[i:j+1], end=" ")
    print()