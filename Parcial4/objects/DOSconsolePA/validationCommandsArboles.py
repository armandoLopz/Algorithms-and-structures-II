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
    
    #METHODS
        
    def validationFolder(self,folderList, nameFolder):

        for folder in folderList.__iter__():

            if nameFolder.lower() == folder.getNameFolder().lower():
                
                return folder.getFolderList()

        return None
    
    #Valida si la unidad se encuentra en la lista enlazada de unidades
    def validationUnit(self, needFolderUnit):
        
        for unit in self.__unit :

            if self.__args[0].lower() == unit.getNameUnit().lower():

                #Devuelve la folderlist de la unidad encontrada para futuras operaciones
                if needFolderUnit:
                    
                    return unit.getFolderList()
                
                return True
        
        return None