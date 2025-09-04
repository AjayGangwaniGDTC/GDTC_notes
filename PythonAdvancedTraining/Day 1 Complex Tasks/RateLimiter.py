# Scenario: You want to limit how many times a user can perform an action (e.g., downloading a certificate) within a time window.

import time
import functools

def rate_limiter(max_calls, per_seconds):
    def decorator(func):
        calls = 0
        reset = time.time()
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal calls, reset
            
            #Calculate the elapsed time
            elapsed = time.time() - reset
            
            #Check whether the elapsed time is greater than period
            if elapsed > per_seconds:
                calls=0
                reset=time.time()
             
            #Checks if the maximum calls are reached or not    
            if calls >= max_calls:
                raise ValueError("Cannot make more calls now please try again after some time...")
            
            calls +=1
            return func(*args, **kwargs)
        return wrapper
    return decorator
                
        
@rate_limiter(max_calls=8, per_seconds=10)
def api_calls():
    print("API call successfull...")
    
for i in range(12):
    try:
        api_calls()
    except ValueError as e:
        print(f"Error occured:",e)