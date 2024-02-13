import objects.SystemComponents.file as file
import objects.SystemComponents.folder as folder
from objects.TDA.Cola import cola  
from objects.TDA.Pila import pila
from objects.TDA.LinkedList import linkedList
import datetime
import json

class upload:
    
    def __init__(self, unit):

        self.__file = file.file
        self.__unit = unit
        self.__folder = folder.folder

        self.__colaJson = cola.Cola()
        self.__colaTxt = cola.Cola()

        self.__pila = pila.Pila()
        self.__linkedlist = linkedList.ListaEnlazada()

    #Creacion de las funciones que se encargan de la carga de archivos JSON y Txt
    def datosJson(self):

        pathFile = r"Parcial4\contFiles\archivo.json"
        
        with open(pathFile, 'r') as archivo:

            datosJson = json.load(archivo)

            return datosJson
    
    def datosJsonTxt(self):

        pathFile = r"Parcial4\contFiles\archivo2.json"
        
        with open(pathFile, 'r') as archivo:

            datosJson = json.load(archivo)

            return datosJson
    
    #Creacion de las funciones que se encargan de la instanciacion de de los archivos 
                
    def createFilesJson(self):

        contentJsonFiles = self.datosJson()
        #Inicializa la cola que se va a utilizar y devolver en el metodo

        listfiles = [
            contentJsonFiles["archivo1"],
            contentJsonFiles["archivo2"],
            contentJsonFiles["archivo3"],
            contentJsonFiles["archivo4"],
            contentJsonFiles["archivo5"]
        ]

        for data in listfiles:

            file = self.__file(
                data["id"],
                data["name"],
                data["size"],
                data["extension"],
                data["creationDate"],
                data["content"],
                data["modificationDate"]
            )

            self.__colaJson.agregar(file)
        
        return self.__colaJson
    
    def createFilesTxt(self):

        contentJsonFiles = self.datosJsonTxt()
        #Inicializa la cola que se va a utilizar y devolver en el metodo

        listfiles = [
            contentJsonFiles["archivo1"],
            contentJsonFiles["archivo2"],
            contentJsonFiles["archivo3"],
            contentJsonFiles["archivo4"],
            contentJsonFiles["archivo5"]
        ]

        for data in listfiles:

            file = self.__file(
                data["id"],
                data["name"],
                data["size"],
                data["extension"],
                data["creationDate"],
                data["content"],
                data["modificationDate"]
            )

            self.__colaTxt.agregar(file)

        return self.__colaTxt
    
    #Creacion de las funciones que se encargan de la instanciacion de las carpetas 

    def createsubFoldersTxt(self):

        file1 = self.createFilesTxt()

        folder1 = self.__folder(1,"ArchivosTXT", 400, datetime.datetime.now, file1, None)
        folder2 = self.__folder(2,"AnotacionesViajes", 300, datetime.datetime.now, file1, None)
        #folder3 = self.__folder(3,"Contenido_audiovisual", 1400, datetime.datetime.now, file, None)
        #folder4 = self.__folder(4,"Clases_curso", 1500, datetime.datetime.now, file, None)

        listFolders = [folder1, folder2]
        
        for folder.folder in listFolders:

            self.__pila.agregar(folder.folder)

        return self.__pila
    
    def createFolder(self):
        
        subFolders = self.createsubFoldersTxt()
        file = self.createFilesJson()

        folder1 = self.__folder(1,"ArchivosJSON", 400, datetime.datetime.now, file, subFolders)
        folder2 = self.__folder(2,"ImagenesFamilia", 300, datetime.datetime.now, file, subFolders)
        folder3 = self.__folder(3,"ContenidoPDF", 1400, datetime.datetime.now, file, None)
        folder4 = self.__folder(4,"Clases universidad", 1500, datetime.datetime.now, file, subFolders)

        listFolders = [folder1, folder2, folder3, folder4]
        
        for folder.folder in listFolders:

            self.__linkedlist.agregar(folder.folder)

        return self.__linkedlist
    
    #Creacion de la unidad que se ejecutara en la consolaDOS
    
    def createUnit(self):

        return self.__unit(1,"C:", 1024, 800, "SSD", self.createFolder())