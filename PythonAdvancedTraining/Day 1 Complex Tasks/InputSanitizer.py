import functools

def sanitize_input(rules: dict):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            result = func(*args, **kwargs)
            new_string = ''
            for i in result:
                # if the remove rules are there and also strip is true then we won't do anything
                if i in rules['remove'] and rules['strip']:
                    continue
                else:
                    new_string += i
            return new_string
        return wrapper
    return decorator

@sanitize_input({'remove': ['$', '#'], 'strip': False})        
def take_input():
    return input("Enter your string:")

print(take_input())