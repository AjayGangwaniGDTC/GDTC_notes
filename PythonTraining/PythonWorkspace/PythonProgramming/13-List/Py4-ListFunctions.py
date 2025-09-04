lst = [12, 124, 'Python', True, 100]
print(lst, type(lst))

print(lst[1:4])

lst[1] = 'This is a list'
lst.append('last element')
print(lst)
print(len(lst))

odd = [1, 3, 5, 7, 9]
even = [2, 4, 6, 8]
num = [odd, even]
print(num)
print(num[1][0])

list1 = list([12, 3, 4, 67])
print(list1, type(list1))