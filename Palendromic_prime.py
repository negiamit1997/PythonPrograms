#palendromic prime
num = 121


reverse = int(str(num)[::-1])

if reverse == num:
    if num > 1:
        for i in range(2,num):
            if num%i ==0:
                print("Number is not prime, but palendromic")
                break;
        else:
            print("Number is prime and palendromic")

else:
    if num > 1:
        for i in range(2,num):
            if num%i ==0:
                print("Number is not prime and not palendromic")
                break;
        else:
            print("Number is prime but not palendromic")