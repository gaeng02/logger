import os

class LoggerConfig :

    def __init__ (self) :
        print("Testing :: LoggerConfig creation")
        
        self.file = "config"

        if os.path.exists(self.file) :
            self.__read_config()
        else : self.__initialize()
        
        print("Completed :: LoggerConfig creation")

    def __initialize (self) : 
        f = open(self.file, "w")
        f.close ()

        self.filepath = "./data/log"
        self.log_format = "[{time}] [{level}] {message}"
        self.time_format = ""
        self.level = "DEBUG"
        self.__save()
        

    def _set (self, filepath = False, log_format = False, time_format = False, level = False) :

        if filepath : self.filepath = filepath
        if log_format : self.log_format = log_format
        if time_format : self.time_format = time_format
        if level and (level in self.LEVELS) : self.level = level

        self.__save()

    def __save (self) :
        config_args = {
            "filepath" : self.filepath,
            "log_format" : self.log_format,
            "time_format" : self.time_format,
            "level" : self.level
        }
        
        with open(self.file, "w") as f :
            for key, value in config_args.items() :
                f.write(f"{key:<15} :: {value}\n")
                
        f = open(self.filepath, "w")
        f.close ()
        

    def __read_config (self) :
        # parsing
        with open (self.file, "r") as f :
            content = f.read()
            
        params = content.split("\n")
        self.filepath = params[0][15:]
        self.log_format = params[1][15:]
        self.time_format = params[2][15:]
        self.level = params[3][15:]
        

    def _print_config (self) :
        with open (self.file, "r") as f :
            content = f.read()
            print(content)

    def _print_data (self) :
        with open (self.file, "r") as f :
            content = f.read()

        params = content.split("\n")
        self.filepath = params[0][15:]
        self.log_format = params[1][15:]
        self.time_format = params[2][15:]
        self.level = params[3][15:]

        print(self.filepath)
        print(self.log_format)
        print(self.time_format)
        print(self.level)
        

    def _get_filepath (self) :
        return self.filepath

    def _get_log_format (self) :
        return self.log_format
    
    def _get_time_format (self) :
        return self.time_format

    def _get_level (self) :
        return self.level

        
            
class Logger :

    LEVELS = {"DEBUG" : 1, "INFO" : 2, "WARNING" : 3, "ERROR" : 4, "EMERGENCY" : 5}
    
    def __init__ (self) :
        print("Testing :: Logger creation")
        
        self.config = LoggerConfig()
        self.file = self.config._get_filepath()
        self.log_format = self.config._get_log_format()
        self.time_format = self.config._get_time_format()
        self.level = self.config._get_level()
        
        print("Completed :: Logger creation")

    def set (self, filepath = False, log_format = False, time_format = False, level = False) :
        self.config._set(filepath, _format, level)
        self.file = self.config._get_filepath()
        self.log_format = self.config._get_log_format()
        self.time_format = self.config._get_time_format()
        self.level = self.config._get_level()

    def log (self, comment, level = False) :
        if not level : level = self.level

        time = os.popen("date {time_format}").read().strip()

        # issue : format has 2 meanings. 
        # time format or logging format
        sentence = self.log_format.format(time = time, level = level, message = comment) + "\n"

        with open (self.file, "w") as f :
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
        
        for key, value in self.LEVELS :
            print(key, value)

    def _print_path (self) :
        print(os.getcwd())
        
