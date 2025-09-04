#raise is used to manually throw an exception if the age is invalid
def check_age(age):
    if age < 18:
        raise ValueError('Age must be greater than 18')
    else:
        print('You are eligible to drive')

try:
    age = int(input('Enter you age:'))
    check_age(age)
except ValueError as e:
    print('Error:', e)