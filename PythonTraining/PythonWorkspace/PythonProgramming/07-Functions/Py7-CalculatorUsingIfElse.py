def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

print('Welcome to Simple Calculator')
num1 = int(input('Enter Number 1:'))
num2 = int(input('Enter Number 2:'))
choice = int(input('Enter Your Choice(1. Addition, 2. Subtraction, 3. Multiplication, 4. Division):'))

if choice == 1:
    print('The addition of', num1, 'and', num2, 'is:', add(num1, num2))
elif choice == 2:
    print('The subtraction of', num1, 'and', num2, 'is:', sub(num1, num2))
elif choice == 3:
    print('The multiplication of', num1, 'and', num2, 'is:', mul(num1, num2))
elif choice == 4:
    print('The division of', num1, 'and', num2, 'is:', div(num1, num2))
else:
    print('Invalid Choice')