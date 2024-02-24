#Sum of Numbers using for loop or while loop
#Using for loop
n=int(input("Enter the number:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("The sum of first",n,"numbers is",sum)
#Using while loop
n=int(input("Enter the number:"))
sum=0
i=1
while i<=n:
    sum=sum+i
    i=i+1
print("The sum of first",n,"numbers is",sum)