'''This is the file to create decorator for logging each and every transaction in the log file'''

import time
import functools
from .config import logger

def log_phase(phase_name):
    '''This function is taking the phase_name as parameter to specify in which 
    phase we are currently present'''
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            logger.info("%s started", phase_name)
            start_time = time.time()
            try:
                result=func(*args,**kwargs)
                duration = time.time() - start_time
                logger.info("%s completed in %.2fs", phase_name, duration)
                return result
            except Exception as e:
                logger.error("Error during %s: %s", phase_name, e)
                raise
        return wrapper
    return decorator
