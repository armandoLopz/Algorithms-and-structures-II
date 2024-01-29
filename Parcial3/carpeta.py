class carpeta:

    def __init__(self, id, name, totalSize, creationDate, fileList = [], foldersList = []):

        self.__id = id
        self.__name = name
        self.__fileList = fileList
        self.__creationDate = creationDate
        self.foldersList = foldersList
        self.__totalSize = totalSize

    
    #METHODS
    def addFileToCarpet(self, fichero):

        self.__fileList.append(fichero)
    
    def contentFolder(self):
        
        for fichero in self.__fileList:

            fichero.showDetailsFile()

    #GETTERS 
    
    def getIdCarpeta(self):

        return self.__id
    
    def getNameCarpeta(self):

        return self.__name
    
    def getTotalSizeCarpeta(self):

        return self.__totalSize
    
    def getCreationDateCarpeta(self):

        return self.__creationDate
    
    """def getFileListCarpeta(self):

        return self.fileList"""
    
    #SETTERS 

    def setIdCarpeta(self, id):

        self.__id = id

    def setNameCarpeta(self, name):

        self.__name = name

    def setCreationDateCarpeta(self, creationDate):

        self.__creationDate = creationDate

    def setTotalSizeCarpeta(self, totalSize):

        self.__totalSize = totalSize
    
    def setFileList(self, fileList = []):

        self.__fileList = fileList