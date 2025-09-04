import functools

def environment_mode(environment):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            msg = (f"You are currently working in {environment} environment and have started executing function {func.__name__}()")
            result = func(*args, **kwargs)
            #Checking for each run and granting the permissions accordingly
            try: 
                if environment=="production":
                    print("Access Granted")
                    print(msg)
                    print("You can access the database and start modifying it")
                    return result
                elif environment=="development":
                    print("Access Granted")
                    print(msg)
                    print("You can modify the log files and also you can access the database for modification")
                    return result
                elif environment=="testing":
                    print("Access Granted")
                    print(msg)
                    print("You can access the code in dry run mode for testing purposes")
                    return result
                else:
                    raise ValueError("Invalid environment")
            except ValueError as e:
                print("Error occurred: ")
                return e
            
        return wrapper
    return decorator

                        
@environment_mode(environment="development")
def project():
    return "You have successfully made changes..."
    
print(project())