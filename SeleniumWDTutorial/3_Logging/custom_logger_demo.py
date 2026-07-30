import custom_logger as cl

class Loggingdemo2():

    log = cl.customLogger("DEBUG")

    def method1(self):
        self.log.debug("This is a debug message from method1")
        self.log.info("This is an info message from method1")
        self.log.warning("This is a warning message from method1") 
        self.log.error("This is an error message from method1")
        self.log.critical("This is a critical message from method1")

    def method2(self):
        m2logger = cl.customLogger("INFO")
        m2logger.debug("This is a debug message from method2")
        m2logger.info("This is an info message from method2")
        m2logger.warning("This is a warning message from method2")
        m2logger.error("This is an error message from method2")
        m2logger.critical("This is a critical message from method2")

    def method3(self):
        m3logger = cl.customLogger("ERROR")
        m3logger.debug("This is a debug message from method3")
        m3logger.info("This is an info message from method3")
        m3logger.warning("This is a warning message from method3")
        m3logger.error("This is an error message from method3")
        m3logger.critical("This is a critical message from method3")

demo = Loggingdemo2()
demo.method1()
demo.method2()
demo.method3()