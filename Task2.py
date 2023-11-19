#program to create a simple calculator
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
print('Select the desired operation - ')
print('A - addition')
print('B - Subtraction')
print('C - Multiplication')
print('D - Division')
choice = input('Enter your choice - (A/B/C/D)')
a = int(input('Enter the first number - '))
b = int(input('Enter the second number - '))
if choice=='A':
    print(a ,'+', b ,'=', add(a,b))
elif choice=='B':
    print(a ,'-', b, '=', sub(a,b))
elif choice=='C':
    print(a ,'*', b, '=', multiply(a,b))
elif choice=='D':
    print(a, '/', b, '=', divide(a,b))
else:
    print('Invalid Choice. Please select any of the valid choices.')





