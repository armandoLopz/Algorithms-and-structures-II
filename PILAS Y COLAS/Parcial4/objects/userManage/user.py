class user:

    def __init__(self, id, name, lastName, cedula, rol):

        self.__id = id
        self.__name = name
        self.__lastName = lastName
        self.__cedula = cedula
        self.__rol = rol

    #METHOD
    
    def createUser():
        
        print("Ingrese los siguientes datos")
        idUser = int(input("ID: "))
        nameUser = input("Nombre: ")
        lastNameUser = input("Apellido: ")
        cedulaUser = int(input("Cedula: "))
        rolUser = "user"

        userCreate = True

        if userCreate:

            user1 = user(idUser,nameUser,lastNameUser,cedulaUser, rolUser)
            return userCreate, user1
                
        else:

            return userCreate, None
            

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