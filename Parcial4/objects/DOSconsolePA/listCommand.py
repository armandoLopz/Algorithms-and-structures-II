from . import command
from objects.SystemComponents.folder import folder as fl
from objects.SystemComponents.file import file 

import sys

class DirCommand(command.command):  
    #El metodo execute sirve para ejecutar toda la accion que hace el
    # comando al ser llamado desde la consola
    def execute(unit):

        #print(f"ARCHIVOS DE LA unidad {unit.getNameUnit()}") 
        return unit.contentUnit()
            
class ExitCommand(command.command):
    def execute():
        print("Saliendo...")
        sys.exit()
        #Ejemplo de comando ayuda

class HelpCommand(command.command):
    def execute():
        print("Comandos disponibles:")
        print("dir - Lista los archivos en el directorio actual")
        print("echo [mensaje] - Repite el mensaje")
        print("exit - Sale de la consola")
        print("help - Muestra esta ayuda")

class Cd(command.command):
    def execute(listFiles, raizFiles, listSub):
        
        try:   
            print("Ingrese la accion que desea realizar ")
            print("2- Agregar Archivo ")
            print("3- Agregar subcarpeta")
            print("4- Regresar al directorio padre")

            decition = int(input())

            if decition == 2:

                nameFile = input("Ingrese el nombre del archivo")
                newFile = file(0, nameFile ,0, ".txt", None, None, None)

                listFiles.insertar(newFile, raizFiles)

                return print("Se agrego el archivo con exito")
            
            elif decition == 3:

                nameFolder = input("Ingrese el nombre de la carpeta")
                newFolder = fl(0,nameFolder, 0,None,None,None)
                listSub.insertar(newFolder)
                return print("Se agrego el folder a la carpeta SubFolder con exito")
            
            elif decition == 4:
                
                return print("Regreso al directorio padre con exito")
            
            else:

                return print("Seleccione una opcion valida")

        except:
            return print("Seleccione una opcion valida")
    
        
class Mkdir(command.command):

    def execute(list, folder, size):

        if size == 4:

            list.insertar(folder)
            return print("La carpeta ha sido creada con exito")
        
        for unit in list:
       
            unit.getFolderList().insertar(folder)
            return print("La carpeta ha sido creada con exito")


class type(command.command):

    def execute(size, file , unit):

        if size == 3:

            listFolder = None
            listFile = None
            raiz = None

            for unit in unit.__iter__():

                listFolder = unit.getFolderList()
                break

            for folder in listFolder:

                listFile =  folder.getFileListFolder()
                break
            
            raiz = listFile.getRaiz()
   
            listFile.insertar(file, raiz)

            return print("Se agrego el archivo con exito")
        
        if size == 6: 

            raiz = unit.getRaiz()
            unit.insertar(file, raiz)
            return print("Se agrego el archivo con exito")


class rmdir(command.command):
    
    def execute(sizecommand,list, nameFolder):

            trashFolder = fl
            correctFolder = False

            for folder in list.__iter__():
                
                if nameFolder.lower() == folder.getNameFolder().lower():
                        
                    filesDelete = folder.getFileListFolder()
                    subFolderDelete = folder.getFolderList()
                    trashFolder = fl(None, "Papelera", None, None, filesDelete, subFolderDelete)

                    list.eliminar_folder_por_nombre(folder.getNameFolder())
                    list.insertar(trashFolder)

                    correctFolder = False
                    return print("Se elimino el archivo correctamente")
                
            if correctFolder == False:

                return print("Ingrese una carpeta valida en la unidad")