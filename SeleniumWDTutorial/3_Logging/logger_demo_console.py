from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LoggerDemoConsole():

    def testLog(self):
        # create Logger
        # __name__ is a special variable in Python that represents the name of the current module.
        logger = logging.getLogger(LoggerDemoConsole.__name__)
        logger.setLevel(logging.DEBUG)
        logger.propagate = False
        logger.handlers.clear()

        # Create console handler and set level to info
        chandler = logging.StreamHandler()
        chandler.setLevel(logging.INFO)

        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
                                      datefmt='%d-%m-%Y %H:%M:%S')
        
        # Add formatter to console handler => chandler
        chandler.setFormatter(formatter)

        # Add console handler to logger
        logger.addHandler(chandler)

        # Logging messages with different severity levels
        logger.debug("DEBUG message")
        logger.info("INFO message")
        logger.warning("WARNING message")
        logger.error("ERROR message")
        logger.critical("CRITICAL message")

logger_demo = LoggerDemoConsole()
logger_demo.testLog()