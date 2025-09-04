try:
    print("One")
    a = -10
    b = 2
    result = a / b
    print('Result:', result)

    myData = [1, 2, 3, 4, 5]
    print(myData[10])
    print('End')
except ZeroDivisionError:
    print('You cannot divide by zero')
except Exception as e:
    print('some error in code')
    print(e)
else:
    print('Everything is going good! No error in the code')