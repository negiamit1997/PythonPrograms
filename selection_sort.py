#selection sort
#1. find out min value
#2. swap the smallest value to 0th index


#with using min function
"""
list1 = [0,4,5,77,22,66,34,90,900,100,89,3,5,22,0,1]

for i in range(len(list1)):
    min_value = min(list1[i:])
    min_index = list1.index(min_value,i)


    if list1[i] != list1[min_index]:
        list1[i], list1[min_index] =list1[min_index], list1[i]

print(list1)"""


#without using min function

list2 = [0,4,5,77,22,66,34,90,900,100]

for i in range(len(list2)):
    m = i
    for j in range(i+1, len(list2)):
        if list2[j] < list2[i]:
         m = j

    list2[i], list2[m] = list2[m], list2[i]

print(list2)
