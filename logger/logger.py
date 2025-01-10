class LoggerConfig :

    def __init__ (self) :
        self.file = "log"
        self._initialize()

    def _initialize (self) : 
        f = open(self.file, "w")
        f.close ()

    def _print (self) :
        with open (self.file, "r") as f :
            content = f.read()
            print(content)
            
class Logger :

    def __init__ (self) :
        self.config = LoggerConfig()
