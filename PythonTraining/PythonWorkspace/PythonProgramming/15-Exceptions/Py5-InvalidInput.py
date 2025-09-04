try:
    num1 = int(input('Enter first number:'))
    num2 = int(input('Enter second number:'))

    result = num1 / num2
    print('Result:', result)
except ZeroDivisionError:
    print('You cannot divide by zero')
except ValueError as e:
    print('Please enter a valid number', e)
else:
    print('No error')
finally:
    print('All done!')