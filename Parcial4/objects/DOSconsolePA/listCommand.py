from . import command
from objects.SystemComponents.folder import folder as fl
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
    def execute():
        #AGREGAR LAS ACCIONES QUE SE PUEDEN HACER EN EL DIRECTORIO ESTABLECIDO
        return print("Directorio encontrado")
        
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
            linkedList = unit.getFolderList()
            listFolder = None

            for folder in linkedList.__iter__():

                listFolder = folder.getFileListFolder()
                break

            listFolder.agregar(file)

            return print("Se agrego el archivo con exito")
        
        if size == 5: 

            unit.agregar(file)
            return print("Se agrego el archivo con exito")


class rmdir(command.command):
    
    def execute(sizecommand,list, nameFolder):

        trashFolder = fl
        for folder in list.__iter__():
            
            if nameFolder == folder.getNameFolder().lower():
                    
                filesDelete = folder.getFileListFolder()
                subFolderDelete = folder.getFolderList()
                trashFolder = fl(None, "Papelera", None, None, filesDelete, subFolderDelete)

                list.eliminar(folder)
                list.agregar(trashFolder)
                return print("Se elimino el archivo correctamente")