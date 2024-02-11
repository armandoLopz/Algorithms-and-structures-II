class file:

    def __init__(self, id, name, size, extension, creationDate, modificationDate, content):

        self.__id = id
        self.__name = name
        self.__size = size
        self.__extension = extension
        self.__creationDate = creationDate
        self.__modificationDate = modificationDate
        self.__content = content

    #METHODS
        
    def showDetailsFile(self):

        return f"\n      Nombre: {self.__name}\n      Tipo de extension: {self.__extension}\n      Tamaño: {self.__size}\n      Fecha de modificación: {self.__modificationDate}\n"

    #GETTERS

    def getIdfile(self):

        return self.__id
        
    def getNamefile(self):

        return self.__name
    
    def getSizefile(self):

        return self.__size
    
    def getExtensionfile(self):

        return self.__extension
    
    def getCreateDatefile(self):

        return self.__creationDate
    
    def getEModificationDatefile(self):

        return self.__modificationDate
    
    def getContentfile(self):

        return self.__content
    
    #SETTERS

    def setNamefile(self,name):

        self.__name = name

    def setSizefile(self,size):

        self.__size = size
    
    def setExtensionfile(self,extension):

        self.__extension = extension
    
    def setCreationDatefile(self,creationDate):

        self.__creationDate = creationDate
    
    def setModificationDatefile(self,modificationDate):

        self.__modificationDate = modificationDate

    def setContentfile(self, content):

        self.__content = content