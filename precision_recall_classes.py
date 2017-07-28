class Template(object):
    def __init__(self):
        self._name = None
        self._codes = ""
        self._codetype = ""
        self._numberOfCodes = 0

    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

    def setCodeType(self, codetype):
        self._codetype += codetype

    def getCodeType(self):
        return self._codetype    

    def setCodes(self, codes):
        self._codes += codes

    def getCodes(self):
        return self._codes

    def setNumberOfCodes(self, numberOfCodes):
        self._numberOfCodes += numberOfCodes

    def getNumberOfCodes(self):
        return self._numberOfCodes

class Autocodes(Template):
    def __init__(self): #constructor
        Template.__init__(self)
        self._environment = None
        self._date = None
        self._status = ""
        self._numberMissing = 0
        self._numberAdditional = 0
        self._precision = 0.0
        self._recall = 0.0

    def setEnvironment(self, environment):
        self._environment = environment

    def getEnviroment(self):
        return self._environment

    def setDate(self, date):
        self._date = date

    def getDate(self):
        return self._date

    def getNumberMissing(self):
        return self._name

    def setNumberMissing(self, missing):
        self._numberMissing += missing

    def getNumberAdditional(self):
        return self._numberAdditional

    def setNumberAdditional(self, additional):
        self._numberAdditional += additional

    def getPrecision(self):
        # self._precision =   
        return self._precision

    def getRecall(self):
        # self._recall = 
        return self._recall

    def getStatus(self):  
        return self._status

    def setStatus(self, status):
        self._status += status