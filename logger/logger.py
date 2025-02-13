import os
from datetime import datetime

class LoggerConfig:
    LEVELS = {"DEBUG": 1, "INFO": 2, "WARNING": 3, "ERROR": 4, "EMERGENCY": 5}

    def __init__(self):
        print("Testing :: LoggerConfig creation")

        self.file = "config"

        if os.path.exists(self.file):
            self.__read_config()
        else:
            self.__initialize()

        print("Completed :: LoggerConfig creation")

    def __initialize(self):
        f = open(self.file, "w")
        f.close()

        self._filepath = "./data/log"
        self._log_format = "[{time}] [{level}] {message}"
        self._time_format = "%Y-%m-%d %H:%M:%S"
        self._level = "DEBUG"
        self.__save()

    def _set(self, filepath=False, log_format=False, time_format=False, level=False):
        if filepath:
            self._filepath = filepath
        if log_format:
            self._log_format = log_format
        if time_format:
            self._time_format = time_format
        if level and (level in self.LEVELS):
            self._level = level

        self.__save()

    def __read_config(self):
        config_args = {}

        with open(self.file, "r") as f:
            for line in f:
                parts = line.split("::")
                if len(parts) == 2:
                    key, value = parts[0].strip(), parts[1].strip()
                    config_args[key] = value

        self._filepath = config_args.get("filepath", "./data/log")
        self._log_format = config_args.get("log_format", "[{time}] [{level}] {message}")
        self._time_format = config_args.get("time_format", "%Y-%m-%d %H:%M:%S")
        self._level = config_args.get("level", "DEBUG")

    def __save(self):
        config_args = {
            "filepath": self._filepath,
            "log_format": self._log_format,
            "time_format": self._time_format,
            "level": self._level,
        }

        with open(self.file, "w") as f:
            for key, value in config_args.items():
                f.write(f"{key:<15} :: {value}\n")

        with open(self._filepath, "w") as f:
            f.close()

    @property
    def filepath(self):
        return self._filepath

    @filepath.setter
    def filepath(self, value):
        self._filepath = value 

    @property
    def log_format(self):
        return self._log_format

    @log_format.setter
    def log_format(self, value):
        self._log_format = value

    @property
    def time_format(self):
        return self._time_format

    @time_format.setter
    def time_format(self, value):
        self._time_format = value

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
        
            
class Logger :

    LEVELS = {"DEBUG" : 1, "INFO" : 2, "WARNING" : 3, "ERROR" : 4, "EMERGENCY" : 5}
    
    def __init__ (self) :
        print("Testing :: Logger creation")
        
        self.config = LoggerConfig()
        self.file = self.config.filepath
        self.log_format = self.config.log_format
        self.time_format = self.config.time_format
        self.level = self.config.level
        
        print("Completed :: Logger creation")

    def set (self, filepath = False, log_format = False, time_format = False, level = False) :
        self.config._set(filepath, log_format, time_format, level)
        self.file = self.config.filepath
        self.log_format = self.config.log_format
        self.time_format = self.config.time_format
        self.level = self.config.level

    def log (self, comment, level = False) :

        print(self.file)
        
        if not os.path.exists(os.path.dirname(self.file)) :
            print("ERROR : file doesn't exists")
            return ;
        
        if not level : level = self.level

        time = datetime.now().strftime(self.time_format)

        sentence = self.log_format.format(time = time, level = level, message = comment) + "\n"
        print(sentence)
        
        with open (self.file, "a") as f :
            f.write(sentence)
                
    def copy (self, copyfile) :
        with open (self.file, "r") as f :
            content = f.read()

        with open (copyfile, "w") as f :
            f.write(content)
            
    def print (self) :
        
        with open (self.file, "r") as f :
            content = f.read()
            print(content)

    def print_level (self) :
        
        for items in self.LEVELS :
            print(items)

    def _print_path (self) :
        print(os.getcwd())
        
