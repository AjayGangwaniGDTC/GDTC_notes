import functools
import math

def transform_pipeline(*steps):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            result = func(*args, **kwargs)
            for step in steps:
                result=step(result)
            return result
        return wrapper
    return decorator

def square(a):
    return a * a

def cube(num):
    return num * num * num

def sqrt(a):
    return (math.sqrt(a))

@transform_pipeline(square, cube, sqrt)
def current_function():
    num = int(input("Enter a number: "))
    return num

print(current_function())