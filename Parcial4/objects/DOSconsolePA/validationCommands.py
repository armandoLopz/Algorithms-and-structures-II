class validationCommands: 
    
    def __init__(self, unit = None, sizecommand = None, args = []):
        
        self.__unit = unit
        self.__sizecommand = sizecommand
        self.__args = args

    #GETTERS
    
    def getUnit(self):

        return self.__unit

    def getSizeCommand(self):

        return self.__sizecommand

    def getArg(self):

        return self.__args
       
    #SETTERS
    
    def settSizeCommand(self, sizecommand):

        self.__sizecommand = sizecommand
    
    def setArgs(self, args):

        self.__args = args
    
    def setUnit(self, unit):

        self.__unit = unit

    #Dependiendo de la longitud del comando va a buscar que metodo ejecutar
    #Para evaluar los archivos
         
    def methodExecute(self):

        if self.__sizecommand == 1:

            return 1
        
        elif self.__sizecommand == 3:

            #Se valida la unidad 

            if validationCommands.validationUnit(self.__args, self.__unit):

                return 3
            
            else:

                print("Unidad no encontrada")

        else:

            return False
    
    def validationFiles(args, folder):

        for file in folder.getFileListFolder():

            if args[0].lower() == file.getNamefile():

                #VER QUE PUEDO HACER 
                return True

    
    def validationFolder(args, unit):

        #Validacion de si el archivo ingresado existe en la unidad
        for folder in unit.getFolderList():

            if args[0].lower() == folder.getNameFolder().lower():

                if validationCommands.validationFiles(folder):

                    return True

        return print("Directorio no encontrado")   
    
    def validationUnit(args, unit):

        #Validacion de si la unidad ingresada existe
        if args[0].lower() == unit.getNameUnit().lower():

            if validationCommands.validationFolder(args[1:], unit):
        
                return True

        else:
            return False