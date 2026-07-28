"""
Logging Demo 1
Logging Levels => Useful for filtering logs based on severity
DEBUG => Detailed information, typically of interest only when diagnosing problems
INFO => Confirmation that things are working as expected
WARNING => An indication that something unexpected happened, or indicative of some problem in the near future
ERROR => Due to a more serious problem, the software has not been able to perform some function
CRITICAL => A serious error, indicating that the program itself may be unable to continue running
"""

import logging
import os

# Levels of logging
# DEBUG < INFO < WARNING < ERROR < CRITICAL


# Set the logging level to DEBUG to print all messages
log_file_path = os.path.join(os.path.dirname(__file__), "introduction.log")
logging.basicConfig(level=logging.DEBUG, filename=log_file_path, format='%(asctime)s - %(levelname)s - %(message)s')

# Will not print DEBUG nor INFO messages, only WARNING, ERROR and CRITICAL, unless the logging level is set to DEBUG or INFO
logging.info("This is an info message")
logging.debug("This is a debug message")

logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")