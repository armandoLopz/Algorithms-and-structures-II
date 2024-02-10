import objects.SystemComponents.file as file
import objects.SystemComponents.folder as folder
#import objects.SystemComponents.unit as unit
import datetime
import json

class upload:
    
    def __init__(self, unit):

        #self.__file = file.file
        #self.__folder = folder.folder
        self.__unit = unit
    

    def datosJson(self):

        pathFile = r"Parcial4\contFiles\archivo.json"
        
        with open(pathFile, 'r') as archivo:

            datosJson = json.load(archivo)

            return datosJson
                
    def createFiles(self):

        contentJsonFiles = self.datosJson

        file1 = file.file(contentJsonFiles()["archivo1"]["id"], contentJsonFiles()["archivo1"]["name"], contentJsonFiles()["archivo1"]["size"], contentJsonFiles()["archivo1"]["extension"], contentJsonFiles()["archivo1"]["creationDate"],contentJsonFiles()["archivo1"]["content"], contentJsonFiles()["archivo1"]["modificationDate"])
        file2 = file.file(contentJsonFiles()["archivo2"]["id"], contentJsonFiles()["archivo2"]["name"], contentJsonFiles()["archivo2"]["size"], contentJsonFiles()["archivo2"]["extension"], contentJsonFiles()["archivo2"]["creationDate"],contentJsonFiles()["archivo2"]["content"], contentJsonFiles()["archivo2"]["modificationDate"])
        file3 = file.file(contentJsonFiles()["archivo3"]["id"], contentJsonFiles()["archivo3"]["name"], contentJsonFiles()["archivo3"]["size"], contentJsonFiles()["archivo3"]["extension"], contentJsonFiles()["archivo3"]["creationDate"],contentJsonFiles()["archivo3"]["content"], contentJsonFiles()["archivo3"]["modificationDate"])
        file4 = file.file(contentJsonFiles()["archivo4"]["id"], contentJsonFiles()["archivo4"]["name"], contentJsonFiles()["archivo4"]["size"], contentJsonFiles()["archivo4"]["extension"], contentJsonFiles()["archivo4"]["creationDate"],contentJsonFiles()["archivo4"]["content"], contentJsonFiles()["archivo4"]["modificationDate"])
        file5 = file.file(contentJsonFiles()["archivo5"]["id"], contentJsonFiles()["archivo5"]["name"], contentJsonFiles()["archivo5"]["size"], contentJsonFiles()["archivo5"]["extension"], contentJsonFiles()["archivo5"]["creationDate"],contentJsonFiles()["archivo5"]["content"], contentJsonFiles()["archivo5"]["modificationDate"])

        listfiles = [file1, file2, file3, file4, file5]

        return listfiles
    
    def createFolder(self):

        folder1 = folder.folder(1,"Archivos JSON", 400, datetime.datetime.now, self.createFiles(), None)
        folder2 = folder.folder(2,"Imagenes Familia", 300, datetime.datetime.now, self.createFiles(), None)
        folder3 = folder.folder(3,"Contenido PDF", 1400, datetime.datetime.now, self.createFiles(), None)
        folder4 = folder.folder(4,"Clases universidad", 1500, datetime.datetime.now, self.createFiles(), None)

        listFolders = [folder1, folder2, folder3, folder4]

        return listFolders
    
    def createUnit(self):

        return self.__unit(1,"C:", 1024, 800, "SSD", self.createFolder)
    

