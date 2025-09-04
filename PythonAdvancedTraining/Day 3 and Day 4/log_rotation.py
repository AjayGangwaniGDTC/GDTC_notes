import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

def main():
    #Create a logger
    logger = logging.getLogger('RotatingLogger')
    logger.setLevel(logging.DEBUG)
    
    #Formatter for log messages
    formatter = logging.Formatter("%(asctime)s -  %(levelname)s - %(message)s")
    
    #----Size Based Rotation-----
    size_handler = RotatingFileHandler(
        "sizebased.log",
        maxBytes=1024,
        backupCount=6
    )
    size_handler.setFormatter(formatter) 
    
    #---Time Based Rotation---
    time_handler = TimedRotatingFileHandler(
        "timebased.log",
        when="M",
        interval=2,
        backupCount=5
    )
    time_handler.setFormatter(formatter)
    
    # Add handlers to logger
    logger.addHandler(size_handler)
    logger.addHandler(time_handler)
    
    #Generate log messages
    for i in range(99):
        logger.debug(f"Log messages #{i}")
    
if __name__ == "__main__":
    main()