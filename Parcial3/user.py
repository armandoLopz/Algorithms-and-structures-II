class user:

    def __init__(self, id, name, lastName, cedula, rol):

        self.__id = id
        self.__name = name
        self.__lastName = lastName
        self.__cedula = cedula
        self.__rol = rol

    #GETTERS 
        
    def getIdUser(self):

        return self.__id
        
    def getNameUser(self):

        return self.__name
    
    def getLastNameUser(self):

        return self.__lastName
    
    def getCedulaUser(self):

        return self.__cedula

    def getRolUser(self):

        return self.__rol
    
    #SETTERS 

    def SetIdUser(self, id):

        self.__id = id

    def SetNameUser(self, name):

        self.__name = name
    
    def SetLastNameUser(self, lastName):

        self.__lastName = lastName
    
    def SetCedulaUser(self, cedula):

        self.__cedula = cedula
    
    def SetRolUser(self, rol):

        self.__rol = rol

    