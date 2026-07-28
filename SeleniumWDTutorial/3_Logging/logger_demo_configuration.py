import logging
import logging.config
import os


class LoggerDemoConfiguration():

    def testLog(self):

        # Load logging configuration from a file
        config_path = os.path.join(os.path.dirname(__file__), "logging.conf")
        log_dir = os.path.dirname(__file__)
        log_file = os.path.join(log_dir, "logger_demo_configuration.log").replace("\\", "/")

        logging.config.fileConfig(config_path, defaults={"log_file": log_file})
        logger = logging.getLogger(LoggerDemoConfiguration.__name__)

        # Logging messages with different severity levels
        logger.debug("DEBUG message")
        logger.info("INFO message")
        logger.warning("WARNING message")
        logger.error("ERROR message")
        logger.critical("CRITICAL message")

logger_demo = LoggerDemoConfiguration()
logger_demo.testLog()