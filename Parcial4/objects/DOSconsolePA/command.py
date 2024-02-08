#clase comanndo del cual todos los comandos heredan
class command:
    def __init__(self, nameCommand = None, description = None, requiredRole = None):

        self.__nameCommand = nameCommand
        self.__description = description
        self.__requiredRole = requiredRole
    
    #METHODS
        
    def execute(self):
        raise NotImplementedError("Debe implementar este método")
    
    #GETTERS 
    
    def getNameComando(self):

        return self.__nameCommand
    
    def getDescriptionComando(self):

        return self.__description
    
    def getRequiredRoleComando(self):

        return self.__requiredRole
    
    #SETTERS
    
    def settNameComando(self, name):

        self.__nameCommand = name
    
    def setDescriptionComando(self, description):

        self.__description = description
    
    def setRequiredRoleComando(self, requiredRole):

        self.__requiredRole = requiredRole

