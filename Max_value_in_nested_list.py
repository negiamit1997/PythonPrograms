list1 = [1,3,4,[88,100],3,11,5,[11,8],9,[44,1,22,3],8]

list2= []
for i in list1:
    if type(i) == list:
        for j in i:
            list2.append(j)
    else:
        list2.append(i)


print(list2)

print(max(list2))

