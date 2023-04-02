#binary search



list1 =[2,7,8,19,0,88,34,77,45,90,18,2]

for i in range(len(list1)):
    for j in range(i+1, len(list1)):

        if list1[j] < list1[i]:
            list1[i],list1[j] = list1[j],list1[i]


key = int(input("Enter a key:\n"))

def func_search(list1, key):
    low = 0
    high = len(list1) - 1

    found = False

    while low<= high and not found:
        mid = (low + high) // 2
        if key == list1[mid]:
            found = True
        elif key > list1[mid]:
            low = mid + 1
        else:
            high = mid - 1

    if found == True:
        print("Key is found")
    else:
        print("Key is not found")


d1 = func_search(list1,key)