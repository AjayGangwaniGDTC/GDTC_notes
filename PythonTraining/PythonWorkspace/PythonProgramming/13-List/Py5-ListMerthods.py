num = [10, 20, 30, 40, 50]
n = len(num)
print('Number of elements in num:', n)

num.append(60)
print('Number after appending 60:', num)

num.insert(0,5)
print('Number after inserting 5 at 0th position:', num)

num1 = num.copy()
print('Newly created list num1:', num1)

n1 = num.count(50)
print('No of time 50 found in the list:', n1)

num.remove(50)
print('Number after removing 50 from list:', num)
