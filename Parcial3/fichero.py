class fichero:

    def __init__(self, id, name, size, extension, creationDate, modificationDate, content):

        self.__id = id
        self.__name = name
        self.__size = size
        self.__extension = extension
        self.__creationDate = creationDate
        self.__modificationDate = modificationDate
        self.__content = content

    #GETTERS

    def getIdFichero(self):

        return self.__id
        
    def getNameFichero(self):

        return self.__name
    
    def getSizeFichero(self):

        return self.__size
    
    def getExtensionFichero(self):

        return self.__extension
    
    def getCreateDateFichero(self):

        return self.__creationDate
    
    def getEModificationDateFichero(self):

        return self.__modificationDate
    
    def getContentFichero(self):

        return self.__content
    
    #SETTERS

    def setNameFichero(self,name):

        self.__name = name

    def setSizeFichero(self,size):

        self.__size = size
    
    def setExtensionFichero(self,extension):

        self.__extension = extension
    
    def setCreationDateFichero(self,creationDate):

        self.__creationDate = creationDate
    
    def setModificationDateFichero(self,modificationDate):

        self.__modificationDate = modificationDate

    def setContentFichero(self, content):

        self.__content = content