class unit: 
        
    def __init__(self, id, name, totalCapacity, avaibleStorage, typeUnit, foldersList):

        self.__id = id
        self.__name = name
        self.__totalCapacity = totalCapacity
        self.__avaibleStorage = avaibleStorage
        self.__foldersList = foldersList
        self.__typeUnit = typeUnit

    #METHODS
        
    def contentUnit(self):

        return self.__foldersList.contentLinkedList()
    
    #GETTERS 
    
    def getFolderList(self):

        return self.__foldersList
    
    def getIdUnit(self):

        return self.__id
    
    def getNameUnit(self):

        return self.__name
    
    def getTotalCapacityUnit(self):

        return self.__totalCapacity
    
    def getAvaibleStorageUnit(self):

        return self.__avaibleStorage
    
    def getTypeUntUnit(self):

        return self.__typeUnit
    
    #FALTA GET FOLDERLIST

    #SETTERS 

    def SetIdUnit(self, id):

        self.__id = id

    def SetNameUnit(self, name):

        self.__name = name
    
    def SetTotalCapacityUnit(self, totalCapacity):

        self.__totalCapacity = totalCapacity
    
    def SetTypeUntUnit(self, typeUnit):

        self.__typeUnit = typeUnit
    
    def SetAvaibleStorageUnit(self, avaibleStorage):

        self.__avaibleStorage = avaibleStorage

    def setFolderList(self, foldersList):

        self.__foldersList = foldersList