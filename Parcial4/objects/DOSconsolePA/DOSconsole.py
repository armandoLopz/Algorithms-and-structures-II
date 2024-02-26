from . import listCommand, validationCommandsArboles
from objects.SystemComponents.folder import folder
from objects.SystemComponents.file import file
from objects.TDA.Cola.cola import Cola
from objects.TDA.LinkedList.linkedList import ListaEnlazada 

from objects.TDA.arbol_binario import arbolBinario


import datetime

class DOSConsole:

    def __init__(self, unit, user):

        self.__validationCommands = validationCommandsArboles.validationCommands()
        self.__unit = unit
        self.__commands = listCommand

    #lista de comados disponibles, cuando se agregue un nuevo comando, se carga e esta
        self.__commands = {
            
        "dir": self.__commands.DirCommand,
        "exit": self.__commands.ExitCommand,
        "help": self.__commands.HelpCommand,
        "cd": self.__commands.Cd,
        "mkdir": self.__commands.Mkdir,
        "type": self.__commands.type,
        "rmdir": self.__commands.rmdir
        
        }

#El metodo run se utiliza para correr la consola e iniciar el programa
    def run(self):
        while True:
            try:
    #C: Es la unidad actual
                entrada = input("\\\\> ")

                partes = entrada.split("/")
                comando = partes[0].lower() if partes else None
     
                amountInput = len(partes)
                args = partes[1:]

                #Se le da valor a lOS parametroS del objeto que valida los comandos
                self.__validationCommands.setUnit(self.__unit)
                self.__validationCommands.setNameCommand(comando)
                self.__validationCommands.setSizeCommand(amountInput)
                self.__validationCommands.setArgs(args)

    #Se busca si el comando existe en la lista definida previamente
                if comando in self.__commands:

                    if comando == "rmdir":

                        if amountInput == 2:

                            if self.__validationCommands.methodExecute():
                                list = ListaEnlazada
                                list = self.__unit.getFolderList()
                                nameFolder = "".join(args[0])
                    
                                self.__commands[comando].execute(amountInput, list, nameFolder)

                    if comando == "type":

                        if amountInput == 3:

                            value = args[0].split(".")
                            nameFile = value[0]
                            extensionFile = value[1]
                            content = args[1]
                            newFile = file(None,nameFile,None, extensionFile,datetime.datetime.now,None,content)

                            self.__commands[comando].execute(self.__validationCommands.getSizeCommand(), newFile, self.__unit)  

                        if amountInput == 5:

                            value = args[2].split(".")
                            nameFile = value[0]
                            extensionFile = value[1]
                            content = args[3]

                            newFile = file(None,nameFile,None, extensionFile,datetime.datetime.now,None,content)

                            newArgs = "".join(args[0])
                            newArgs2 = "".join(args[1])

                            defArgs = (newArgs + " " + newArgs2).split(" ")
                            nameFolder = "".join(newArgs2)

                            self.__validationCommands.setArgs(defArgs)

                            exist = False
                            fileList = Cola
                            exist, fileList = self.__validationCommands.methodExecute()
                            if exist:

                                self.__commands[comando].execute(self.__validationCommands.getSizeCommand(),newFile, fileList)

                            else:

                                print("Debe ingresar una ruta valida")


                    
                    #EJECUTA EL COMANDO DIR
                    if comando == "dir":

                        self.__commands[comando].execute(self.__unit)

                    #EJECUTA EL COMANDO CD
                    if comando == "cd":
                        
                        #MOSTRAR LAS DISTINTAS ACCIONES QUE SE PUEDEN REALIZAR
                        if self.__validationCommands.methodExecute():

                            return self.__commands[comando].execute()
                    
                    #EJECUTA EL COMANDO MKDIR
                    if comando == "mkdir":

                        needFolderUnit = False
                        
                        if amountInput == 2:

                            if folder1 is None and self.__unit is None:

                                print("Ingrese una ruta valida para crear una nueva carpeta")
                            
                            if folder1 is not None and self.__unit is not None:
                                
                                folder1 = folder(0,partes[1],None,None,None,None)
                                self.__commands[comando].execute(self.__unit, folder1, None)

                        if amountInput == 3:

                            if self.__validationCommands.validationUnit(needFolderUnit):

                                folder1 = folder(0,partes[2],None,None,None,None)
                                self.__commands[comando].execute(self.__unit, folder1,None)
                            
                            else:
                                print("Unidad no encontrada")
                        
                        if amountInput == 4:

                            folder1 = folder(0,partes[3],None,None,None,None)

                            needFolderUnit = True
                            listFolderUnit = arbolBinario.ArbolBinario 

                            listFolderUnit =  self.__validationCommands.validationUnit(needFolderUnit)

                            if listFolderUnit is not None:
                                
                                sublistFolder = arbolBinario.ArbolBinario()

                                sublistFolder =  self.__validationCommands.validationFolder(listFolderUnit, partes[2])

                                if sublistFolder is not None:

                                    self.__commands[comando].execute(sublistFolder, folder1, amountInput)
                                
                                else:

                                    print("Carpeta no encontrada")

                            else:
                                print("Unidad no encontrada")
                            
                else:
                    print(f"Comando desconocido: {comando}")

            except KeyboardInterrupt:
                    print("\nOperación cancelada por el usuario.")
                    break
            #except Exception as e:
                    #print(f"Error: {e}")