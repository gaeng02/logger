from Logger import logger

logger.log("Hello World") # Default 

logger.print_level() 
logger.log("INFO", "Hello World")

logger.set(level = "WARNING")
logger.set(filepath = "./test_log")

logger.print()
logger.copy("../copy_log")
