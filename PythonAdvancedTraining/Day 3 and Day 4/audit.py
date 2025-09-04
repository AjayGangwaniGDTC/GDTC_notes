import functools
import logging
import datetime



def log_action(log_level,user,course):
    logging.basicConfig(filename="audittrail.log",
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        filemode='a+',
                        level=logging.DEBUG)
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            msg = f"User {user} have executed function {func.__name__}() and updated the course {course}"
            print(msg)
            result = func(*args,**kwargs)
            if log_level=='INFO':
                logging.info(f"{log_level}, {msg}")
            elif log_level=='DEBUG':
                logging.debug(f"{log_level}, {msg}")
            elif log_level=='WARNING':
                logging.debug(f"{log_level}, {msg}")
            elif log_level=='ERROR':
                logging.error(f"{log_level}, {msg}")
            elif log_level=='CRITICAL':
                logging.critical(f"{log_level}, {msg}")
            else:
                logging.info("Wrong level selected")
            return result
        return wrapper
    return decorator
                
def main():
    user = input("Enter your name: ")
    course = input("Enter the course name you want to modify: ")
    @log_action(log_level='ERROR',user=user,course=course)
    def user_action(user_name, course):
        print(f"Hello user {user_name} you have successfully modified the course {course}")
    user_action(user_name = user, course = course)
    
if __name__ == "__main__":
    main()