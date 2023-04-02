list1 = [1,1,1,2,3,6,7,4,7,9,1,4,6,0,3,6,8,3,4,5]

list2=[]

for i in range(len(list1)):
    if list1[i] == 3:
        list2.append(i)


print(list2)

