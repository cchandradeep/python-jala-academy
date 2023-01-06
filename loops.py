for i in range(10):
    print("Bright IT Career")

# Program to equal operator and not equal operators
firstNumber = int(input("enter a first number :"))
secondNumber =int(input("enter a second number :"))

print(firstNumber != secondNumber)#not equal operator
print(firstNumber == secondNumber)#equal operator


# Write a program to print the odd and even numbers

if firstNumber==0:
    print('null')
elif (firstNumber%2)==0:
    print("even number")
else:
    print('odd number')
# Write a program to print largest number among three numbers

a = int(input('Enter first number  : '))
b = int(input('Enter second number : '))
c = int(input('Enter third number  : '))

if a > b and a > c :
    largest = a
elif b > c :
    largest = b
else :
    largest = c

print(largest, "is the largest of three numbers.")

# Write a program to print even number between 10 and 20 using while


i = 10
while i < 20:
    if i % 2 == 0:
        print(i, end=" ")
    i = i + 1

#  Write a program to print 1 to 10 using the do-while loop statement.

# do while loop doesnt exist in python'

# armstrong number

n = int(input("Enter a number: "))

#initialize the sum
s = 0
t = n

while t > 0:

   digit = t % 10

   s += digit ** 3

   t //= 10

# display the result

if n == s:

   print(n,"is an Armstrong number")

else:

   print(n,"is not an Armstrong number")

# program for prime number

Number=int(input("enter a number to check wether number is prime or not :"))
if Number == 1:
    print ("1 is not a prime number")
elif Number > 1:
    for i in range(2,Number):
        if (Number % i)==0:
            print(Number,"is a not a prime number")
            break
else:
    print(Number,"is a prime number")

# palindrome numnber
palindrome_number=int(input("enter the number to check is it a palindrome number :"))
temp = palindrome_number
rev =0
while(palindrome_number>0):
    dig=palindrome_number%10
    rev=rev*10+dig
    num=num//10

if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")







