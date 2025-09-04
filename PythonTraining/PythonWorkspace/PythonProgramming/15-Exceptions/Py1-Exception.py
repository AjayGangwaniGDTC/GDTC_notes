#Divide by Zero Example
try:
    print("One")
    a = -10
    b = 0
    result = a / b
    print('Result:', result)
    print('End')
except ZeroDivisionError:
    print('You cannot divide by zero')