#Function parameters with return values
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

#main code
x = 10
y = 5

# Function calls and storing return values
result_sum = add(x, y)
result_sub = subtract(x, y)
result_mul = multiply(x, y)

#printing the values
print('Addition:', result_sum)
print('Subtraction:', result_sub)
print('Multiplication:', result_mul)