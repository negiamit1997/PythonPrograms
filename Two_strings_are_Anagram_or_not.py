"""an annagram of a string is an another string that contains same characters, only the order of
characters cab be different
"""

"""Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using
all the orignal letter exactly once
"""

str1 = input("Enter string1:\n").lower()
str2 = input("Enter string2:\n").lower()



if len(str1) == len(str2):
    if sorted(str1) == sorted(str2):
        print("String are anagrams")
    else:
        print("Strings are not anagrams")
else:
    print("Strings are not anagrams")