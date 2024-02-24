#Calculator for Basic Operations

def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    return x / y
x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice = input("Enter choice(1/2/3/4):")
if choice == '1':
    print(x,"+",y,"=", add(x,y))
elif choice == '2':
    print(x,"-",y,"=", sub(x,y))
elif choice == '3':
    print(x,"*",y,"=", mul(x,y))
elif choice == '4':
    print(x,"/",y,"=", div(x,y))
else:
    print("Invalid input")