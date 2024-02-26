from objects.SystemComponents.folder import folder
from objects.SystemComponents.file import file


class validationCommands: 
    
    def __init__(self, unit = [], nameCommand = None, sizecommand = None, args = []):
        
        self.__unit = unit
        self.__nameCommand = nameCommand
        self.__sizecommand = sizecommand
        self.__args = args

    #GETTERS
    
    def getUnit(self):

        return self.__unit
    
    def getNameCommand(self):

        return self.__nameCommand

    def getSizeCommand(self):

        return self.__sizecommand

    def getArg(self):

        return self.__args
       
    #SETTERS
    
    def setUnit(self, unit):

        self.__unit = unit
    
    def setNameCommand(self, nameCommand):

        self.__nameCommand = nameCommand

    def setSizeCommand(self, sizecommand):

        self.__sizecommand = sizecommand
    
    def setArgs(self, args):

        self.__args = args
    
    #Valida si la unidad se encuentra en la lista enlazada de unidades
    def validationUnit(self):
        
        for unit in self.__unit :

            if self.__args[0].lower() == unit.getNameUnit().lower():

                return True
        
        return False