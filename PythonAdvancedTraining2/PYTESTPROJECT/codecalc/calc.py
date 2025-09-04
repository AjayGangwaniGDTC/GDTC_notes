# import pytest

def square(n):
    return n*n

def add(a,b):
    return a+b

def divide(a,b):
    if b==0:
        raise ZeroDivisionError
    return a/b

#Integration Testing components
def total_with_tax(amount): #component 1
    return amount*1.05

def generate_bill(user,amount): #component 2
    return f"{user} owes Rs.{amount}"

#Boundary test
def valid_age(age):
    return 18 <= age <= 60

#object state test
class Device:
    def __init__(self):
        self.status="off"
    def toggle(self):
        self.status="on" if self.status=="off" else "off"
                      
#shape and data validation test
import numpy as np
def create_matrix():
    return np.ones((3,3))

#time based testing
import time
def simulate():
    sum(i*i for i in range(10**5))