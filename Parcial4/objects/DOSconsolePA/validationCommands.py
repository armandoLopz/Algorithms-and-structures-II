#from TDA.Cola import cola
#from TDA.LinkedList import linkedList
#from TDA.Pila import pila

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

    def setSizeCommand(self, sizecommand):

        self.__sizecommand = sizecommand
    
    def setArgs(self, args):

        self.__args = args
    

    #Dependiendo de la longitud del comando va a buscar que metodo ejecutar
    #Para evaluar los archivos
         
    def methodExecute(self):

        #VALIDA EL COMANDO CD
        if self.__nameCommand == "cd":

            if self.validationUnit(self.__args, self.__unit):

                return True
    
    def validationFiles(self, args, folder):

        fileList = folder.getFileListFolder()

        for file in fileList.obtener_objetos():

            if args[0].lower() == file.getNamefile():

                return True

    def validationFolder(self, args, unit):

        #Validacion de si el archivo ingresado existe en la unidad
        lista = unit.getFolderList()
        lenArgs = len(args)

        for folder in lista.__iter__():

            #Evalua si la carpeta que se va a manejar es una carpeta padre
            if args[0].lower() == folder.getNameFolder().lower():
                
                #Si el comando posee 2 entradas en este momento indica que tiene subcarpeta
                #Por lo tanto va a verificar si la subcarpeta ingresada existe
                if lenArgs == 2:
                    subFolder = folder.getFolderList()
                    
                    if self.validationSubFolder(subFolder, args[1]):
                        
                        return True
                    
                #Si lenArgs es igual a 1 indica que se esta accediendo a una carpeta padre
                #Valida si la carpeta padre existe en el directorio
                return True
                
        print("Carpeta no encontrada")
        return False  
    
    def validationSubFolder(self, subfolder, args):

        #Valida la subcarpeta de la carpeta padre 
        if subfolder is not None:
            for folder in subfolder.obtener_objetos():

                if args.lower() == folder.getNameFolder().lower():    
                    return True
    
    def validationUnit(self, args, unit):

        #Validacion de si la unidad ingresada es igual a la que se esta usando
        if args[0].lower() == unit.getNameUnit().lower():
                
            return self.validationFolder(args[1:], unit)
        else:
            
            return print("Unidad no encontrada")
