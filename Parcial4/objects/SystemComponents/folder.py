class folder:

    def __init__(self, id, name, totalSize, creationDate, fileList, foldersList):

        self.__id = id
        self.__name = name
        self.__fileList = fileList
        self.__creationDate = creationDate
        self.__folderList = foldersList
        self.__totalSize = totalSize
        
    #METHODS
    
    def getFolderReference(self):
        
        return self

    def addFileToCarpet(self, fichero):

        self.__fileList.append(fichero)
    
    def sizeTotalFolder(self):

        totalSize = 0

        for file in self.__fileList:

            totalSize += file.getSizeFichero()
        
        return totalSize

    def contentFolder(self):

        #Entra en el condicional si no posee archivos ni subcarpetas
        if self.__fileList == None and self.__folderList == None:

            return ""
        
        #Verifica si La carpeta posee subcarpeta
        if self.__folderList == None:

            return self.__fileList.preorden()
        
        #Verifica si la carpeta que se paso como parametro se encuentra vacia

        self.contentSubFolder()

        return self.__fileList.preorden()
        
    def contentSubFolder(self):
        
        return self.__folderList.preorden()
    
    #GETTERS 
    
    def getIdFolder(self):

        return self.__id
    
    def getNameFolder(self):

        return self.__name
    
    def getTotalSizeFolder(self):

        return self.__totalSize
    
    def getCreationDateFolder(self):

        return self.__creationDate
    
    def getFileListFolder(self):

        return self.__fileList
    
    def getFolderList(self):

        return self.__folderList
    
    #SETTERS 

    def setIdFolder(self, id):

        self.__id = id

    def setNameFolder(self, name):

        self.__name = name

    def setCreationFolder(self, creationDate):

        self.__creationDate = creationDate

    def setTotalSizeFolder(self, totalSize):

        self.__totalSize = totalSize
    
    def setFileList(self, fileList):

        self.__fileList = fileList
    
    def setFolderList(self, foldersList):

        self.__folderList = foldersList