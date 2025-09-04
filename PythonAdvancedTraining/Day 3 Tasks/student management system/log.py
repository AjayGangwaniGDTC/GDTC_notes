import logging
import functools

# Logger setup (can be moved to logger_config.py if needed)
logging.basicConfig(filename="student_records.log",
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    level=logging.DEBUG,
                    filemode="a+")
logger = logging.getLogger("student_logger")

def log_operation(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Executing function: {func.__name__}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"Completed function: {func.__name__} - Result: {result}")
            return result
        except Exception as e:
            logger.error(f"Error in function {func.__name__}: {e}")
            print(f"An error occurred: {e}")
            return None
    return wrapper