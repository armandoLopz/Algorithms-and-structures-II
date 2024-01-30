class comando:

    def __init__(self, id , nameCommand, description, requiredRole):

        self.__id = id 
        self.__nameCommand = nameCommand
        self.__description = description
        self.__requiredRole = requiredRole

    #METHODS
        
    def commandDir(self, unidad):

        print(f"ARCHIVOS DE LA UNIDAD {unidad.getNameUnidad()}")
        unidad.contentUnit()
               
    #GETTERS 
    
    def getIdComando(self):

        return self.__id
    
    def getNameComando(self):

        return self.__nameCommand
    
    def getDescriptionComando(self):

        return self.__description
    
    def getRequiredRoleComando(self):

        return self.__requiredRole
    
    #SETTERS

    def setIdComando(self,id):

        self.__id = id
    
    def settNameComando(self, name):

        self.__nameCommand = name
    
    def setDescriptionComando(self, description):

        self.__description = description
    
    def setRequiredRoleComando(self, requiredRole):

        self.__requiredRole = requiredRole