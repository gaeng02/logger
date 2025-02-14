from Logger import logger
import os

logger._print_path()

filepath = logger.file


if not os.path.exists(filepath) :
    print("Not exist")

else :
    print("Exist")

    with open(filepath, "a") as f :
        f.write("test logfile")
