from . import command
import sys

class DirCommand(command.command):  
    #El metodo execute sirve para ejecutar toda la accion que hace el
    # comando al ser llamado desde la consola
    def execute(unit):
        print(f"ARCHIVOS DE LA unidad {unit.getNameUnit()}")
        unit.contentUnit()
            
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