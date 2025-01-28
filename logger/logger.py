import os

class LoggerConfig :

    def __init__ (self) :
        print("Testing :: LoggerConfig creation")
        
        self.file = "log"

        if os.path.exists(self.file) :
            self.__read_config()
        else : self.__initialize()
        
        print("Completed :: LoggerConfig creation")

    def __initialize (self) : 
        f = open(self.file, "w")
        f.close ()

        self.filepath = "../log"
        self._format = "[{time}] [{level}] {message}"
        self.level = "DEBUG"
        self.__save()
        

    def _set (self, filepath = False, _format = False, level = False) :

        if filepath : self.filepath = filepath
        if _format : self._format = _format
        if level and (level in self.LEVELS) : self.level = level

        self.__save()

    def __save (self) :
        config_args = {
            "filepath" : self.filepath,
            "format" : self._format,
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
        self._format = params[1][15:]
        self.level = params[2][15:]
        

    def _print_config (self) :
        with open (self.file, "r") as f :
            content = f.read()
            print(content)

    def _print_data (self) :
        with open (self.file, "r") as f :
            content = f.read()

        params = content.split("\n")
        self.filepath = params[0][15:]
        self._format = params[1][15:]
        self.level = params[2][15:]

        print(self.filepath)
        print(self._format)
        print(self.level)
        

    def _get_filepath (self) :
        return self.filepath

    def _get_format (self) :
        return self._format

    def _get_level (self) :
        return self.level
        
            
class Logger :

    LEVELS = {"DEBUG" : 1, "INFO" : 2, "WARNING" : 3, "ERROR" : 4, "EMERGENCY" : 5}
    
    def __init__ (self) :
        print("Testing :: Logger creation")
        
        self.config = LoggerConfig()
        self.file = self.config._get_filepath()
        self._format = self.config._get_format()
        self.level = self.config._get_level()
        
        print("Completed :: Logger creation")

    def set (self, filepath = False, _format = False, level = False) :
        self.config._set(filepath, _format, level)
        self.file = self.config._get_filepath()
        self._format = self.config._get_format()
        self.level = self.config._get_level()

    def log (self, comment, level = False) :
        if not level : level = self.level

        time = time.time()

        # issue : format has 2 meanings. 
        # time format or logging format
        sentence = self._format.format(time = time, level = level, message = comment) + "\n"

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
        
        for key, value in LEVELS :
            print(key, value)
        
