from TDA.Cola import cola
from TDA.LinkedList import linkedList
from TDA.Pila import pila

class validationCommands: 
    
    def __init__(self, unit = None, nameCommand = None, sizecommand = None, args = []):
        
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

    def settSizeCommand(self, sizecommand):

        self.__sizecommand = sizecommand
    
    def setArgs(self, args):

        self.__args = args
    

    #Dependiendo de la longitud del comando va a buscar que metodo ejecutar
    #Para evaluar los archivos
         
    def methodExecute(self):

        return True
    
    def validationFiles(args, folder):

        for file in folder.getFileListFolder():

            if args[0].lower() == file.getNamefile():

                #VER QUE PUEDO HACER 
                return True

    
    def validationFolder(args, unit):

        #Validacion de si el archivo ingresado existe en la unidad
        lista = unit.getFolderList()

        for folder in lista.__iter__():

            #Evalua si la carpeta que se va a manejar es una carpeta padre
            if args[0].lower() == folder.getNameFolder().lower():

                if validationCommands.validationFiles(folder):

                    return True
                
            subFolder = folder.getFolderList()

            for folder in subFolder.obtener_objetos():
                
                if args[0].lower() == folder.getNameFolder().lower():

                    if validationCommands.validationFiles(folder):

                        return True

        return print("Directorio no encontrado")   
    
    def validationUnit(args, unit):

        #Validacion de si la unidad ingresada es igual a la que se esta usando
        if args[0].lower() == unit.getNameUnit().lower():

            if validationCommands.validationFolder(args[1:], unit):
        
                return True

        else:
            return False
    
    def FolderIsLinkedList(self, unit):

        linkedList1 = unit.getFolderList()

        if isinstance(linkedList1, linkedList.ListaEnlazada):

            return True
        
        else:
            return False

        
