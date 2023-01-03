a=10
b=10
# Arthimetaic functions

c=a+b
d=a-b
e=a*b
f=a/b
print(c,d,e,f)

# increment and decrement operators
a+=5 #a=a+5
print(a)

b-=5 #b=b-5
print(b)

# # two numbers are equal or not 
A=99999.98
B=99999.99
if A==B:
    print(A,"is equal to ",B)
else:
   print(A,"is not equal to",B)


# print the smaller and larger number
lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("Maximum element in the list is :", max(lst), "\nMinimum element in the list is :", min(lst))


