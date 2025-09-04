#Divide by Zero Example
try:
    print('One')
    myData = [1, 2, 3, 4, 5]
    print(myData[10])
    print('End')
except Exception as e:
    print('some error in code')
    print(e)
else:
    print('Everything is going good! No error in the code')