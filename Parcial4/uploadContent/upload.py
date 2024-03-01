import objects.SystemComponents.file as file
import objects.SystemComponents.folder as folder
from objects.TDA.arbol_nario import arbolNario
from objects.TDA.arbol_binario import arbolBinario
import datetime
import json

class upload:
    
    def __init__(self, unit):

        self.__file = file.file
        self.__unit = unit
        self.__folder = folder.folder

        self.__arbolNario = arbolNario.ArbolNArio() 
        self.__arbolNario2 = arbolNario.ArbolNArio()
        self.__arbolNario3 = arbolNario.ArbolNArio()
        self.__arbolNario4 = arbolNario.ArbolNArio()
        self.__arbolNario5 = arbolNario.ArbolNArio()
        self.__arbolNario6 = arbolNario.ArbolNArio()
        
        self.__arbolBinario = arbolBinario.ArbolBinario()
        self.__arbolBinario2 = arbolBinario.ArbolBinario()
        self.__arbolBinario3 = arbolBinario.ArbolBinario()
        self.__arbolBinario4 = arbolBinario.ArbolBinario()

        self.__arbolBinario5 = arbolBinario.ArbolBinario()
        self.__arbolBinario6 = arbolBinario.ArbolBinario()
        self.__arbolBinario7 = arbolBinario.ArbolBinario()

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
        
        dadFile = self.__file(0,"Archivo Padre", 0,".txt", None, None, "ARCHIVO PADRE")
        self.__arbolNario.insertar(dadFile)
        self.__arbolNario2.insertar(dadFile)
        self.__arbolNario3.insertar(dadFile)
        self.__arbolNario4.insertar(dadFile)

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

            self.__arbolNario.insertar(file,dadFile)
            self.__arbolNario2.insertar(file,dadFile)
            self.__arbolNario3.insertar(file,dadFile)
            self.__arbolNario4.insertar(file,dadFile)

        return self.__arbolNario, self.__arbolNario2, self.__arbolNario3, self.__arbolNario4
    
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

        dadFile = self.__file(0,"Archivo Padre", 0,".txt", None, None, "ARCHIVO PADRE")
        self.__arbolNario5.insertar(dadFile)
        self.__arbolNario6.insertar(dadFile)

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

            self.__arbolNario5.insertar(file, dadFile)
            self.__arbolNario6.insertar(file, dadFile)

        return self.__arbolNario5, self.__arbolNario6
    
    #Creacion de las funciones que se encargan de la instanciacion de las carpetas 

    def createsubFoldersTxt(self):

        file1, file2 = self.createFilesTxt()

        folder1 = self.__folder(1,"Ideas", 400, datetime.datetime.now, file1, None)
        folder2 = self.__folder(2,"Archivos Excel", 300, datetime.datetime.now, file2, None)

        listFolders = [folder1, folder2]
        
        folder3 = self.__folder(1,"ARCHIVO SUB", 400, datetime.datetime.now, file1, None)
        folder4 = self.__folder(2,"JUEGOS FUT", 300, datetime.datetime.now, file2, None)
        listSubfolder = [folder3, folder4]

        for folder.folder in listSubfolder:

            self.__arbolBinario6.insertar(folder.folder)
            self.__arbolBinario7.insertar(folder.folder)
        
        folder1.setFolderList(self.__arbolBinario6)
        folder2.setFolderList(self.__arbolBinario7)

        for folder.folder in listFolders:

            self.__arbolBinario.insertar(folder.folder)
            self.__arbolBinario2.insertar(folder.folder)
            self.__arbolBinario3.insertar(folder.folder)
            self.__arbolBinario4.insertar(folder.folder)
    
        return self.__arbolBinario, self.__arbolBinario2, self.__arbolBinario3, self.__arbolBinario4
    
    def createFolder(self):
        
        file1, file2, file3, file4 = self.createFilesJson()  
        subFolders1, subFolders2, subFolders3, subFolders4 = self.createsubFoldersTxt()


        folder1 = self.__folder(1,"Contactos", 400, datetime.datetime.now, file1, subFolders1)
        folder2 = self.__folder(2,"Futuros Proyectos", 300, datetime.datetime.now, file2, subFolders2)
        folder3 = self.__folder(3,"Pensum", 1400, datetime.datetime.now, file3, subFolders3)
        folder4 = self.__folder(4,"Clases Fisica", 1500, datetime.datetime.now, file4, subFolders4)

        listFolders = [folder1, folder2, folder3, folder4]

        dadfolder = self.__folder(0,"Carpeta Padre", None, datetime.datetime.now, None, None)
        self.__arbolBinario.insertar(dadfolder)

        for folder.folder in listFolders:

            self.__arbolBinario5.insertar(folder.folder)
      
        return self.__arbolBinario5
    
    #Creacion de la unidad que se ejecutara en la consolaDOS
    
    def createUnit(self):

        return self.__unit(1,"C:", 1024, 800, "SSD", self.createFolder())