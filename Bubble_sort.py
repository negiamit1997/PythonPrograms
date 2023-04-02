#bubble sort sometime reffers to sinking sort, which sorts n number of elementsin the list by comparing the
#each pairof adjacentitems and swapthem if they are in wrong order
list2 = [0,4,5,77,22,66,34,90,900,100,89,3,5,22,0,1]

for i in range(len(list2)):
    m = i
    for j in range(i+1, len(list2)):
        if list2[i] > list2[j]:
          list2[i],list2[j] = list2[j], list2[i]


print(list2)
