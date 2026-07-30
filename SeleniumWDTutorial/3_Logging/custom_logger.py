import inspect
import logging

def customLogger(loglevel):
    # Gets the name of the class or method from where this method is called
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)

    # Set the logging level based on the provided loglevel argument
    if loglevel == "DEBUG":
        logger.setLevel(logging.DEBUG)
    elif loglevel == "INFO":
        logger.setLevel(logging.INFO)
    elif loglevel == "WARNING":
        logger.setLevel(logging.WARNING)
    elif loglevel == "ERROR":
        logger.setLevel(logging.ERROR)
    elif loglevel == "CRITICAL":
        logger.setLevel(logging.CRITICAL)
    else:
        raise ValueError("Invalid log level: {}".format(loglevel))

    # Create a console handler to output logs to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logger.level)

    # Create a formatter for the log messages
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    # Add the console handler to the logger
    if not logger.handlers:
        logger.addHandler(console_handler)

    return logger