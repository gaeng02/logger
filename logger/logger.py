class LoggerConfig :

    LEVELS = {"DEBUG" : 1, "INFO" : 2, "WARNING" : 3, "ERROR" : 4, "EMERGENCY" : 5}

    def __init__ (self) :
        self.file = "log"
        self.__initialize()

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
        

    def _print (self) :
        with open (self.file, "r") as f :
            content = f.read()
            print(content)
        
            
class Logger :

    def __init__ (self) :
        self.config = LoggerConfig()

    def set (self, filepath = False, _format = False, level = False) :
        self.config._set(filepath, _format, level)

    # def log (self, level = False) :
        

    # def copy (self) : 
