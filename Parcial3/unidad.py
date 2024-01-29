class unidad:

    def __init__(self, id, name, totalCapacity, avaibleStorage, typeUnit, foldersList = []):

        self.__id = id
        self.__name = name
        self.__totalCapacity = totalCapacity
        self.__avaibleStorage = avaibleStorage
        self.__foldersList = foldersList
        self.__typeUnit = typeUnit

    #METHODS
        
    def contentUnit(self):

        for carpeta in self.__foldersList:
            print(f"CONTENIDO DE LA CARPETA: {carpeta.getNameCarpeta()}")
            carpeta.contentFolder()

    #GETTERS 
    
    def getIdUnidad(self):

        return self.__id
    
    def getNameUnidad(self):

        return self.__name
    
    def getTotalCapacityUnidad(self):

        return self.__totalCapacity
    
    def getAvaibleStorageUnidad(self):

        return self.__avaibleStorage
    
    def getTypeUntUnidad(self):

        return self.__typeUnit
    
    #FALTA GET FOLDERLIST

    #SETTERS 

    def SetIdUnidad(self, id):

        self.__id = id

    def SetNameUnidad(self, name):

        self.__name = name
    
    def SettotalCapacityUnidad(self, totalCapacity):

        self.__totalCapacity = totalCapacity
    
    def SetTypeUnitUnidad(self, typeUnit):

        self.__typeUnit = typeUnit
    
    def SetAvaibleStorageUnidad(self, avaibleStorage):

        self.__avaibleStorage = avaibleStorage

    #FALTA SET FOLDERLIST