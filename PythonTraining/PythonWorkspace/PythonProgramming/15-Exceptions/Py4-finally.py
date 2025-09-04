try:
    print("One")
    a = -10
    b = 2
    result = a / b
    print('Result:', result)
    print('End')
except ZeroDivisionError:
    print('You can\'t divide by zero')
finally:
    print('All done!')
