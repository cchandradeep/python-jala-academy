Number=int(input("enter a number to check wether number is prime or not :"))
if Number == 1:
    print ("1 is not a prime number")
elif (Number > 1):
    for i in range(2,Number):
        if (Number % i)==0:
            print(Number,"is a not a prime number")
            break
    else:
        print(Number,"is a prime number")
else:
    print(Number,"is a prime number")