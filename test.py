from Logger import logger

print("Test :: log print")
logger.log("Hello World") # Default 

print("Test :: level print")
logger.print_level() 
logger.log("INFO", "Hello World")

print("Test :: level set")
logger.set(level = "WARNING")

print("Test :: move file")
logger.set(filepath = "./data/test_log")

print("Test :: copy")
logger.copy("./data/copy_log")
