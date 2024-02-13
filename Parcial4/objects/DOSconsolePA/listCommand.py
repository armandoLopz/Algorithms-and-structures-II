from . import command
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
    def execute(self, args):

        print("Se esta ejecutando el comando CD DESDE EL COMANDO")
        
        """amountArgs = len(args)

        print(amountArgs)

        if amountArgs == 3:
            return True"""
        return args
        
class Mkdir(command.command):

    def execute(self, args):

        return True
        

