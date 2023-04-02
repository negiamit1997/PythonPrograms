#Prime Number

num = 2

if num >1:
    for i in range(2, num):
        if num %i ==0:
            print("Number is not prime")
            break;
    else:
        print("Number is prime")




#Printing prime number in sequesnce

lower = int(input("Enter lower limit:\n"))
upper = int(input("Enter lower limit:\n"))


for num in range(lower, upper+1):
    if num>1:
        for i in range(2, num):
            if num % i ==0:
                break
        else:
            print(num)

