from . import listCommand, validationCommandsArboles
from objects.SystemComponents.folder import folder
from objects.SystemComponents.file import file
from objects.TDA.Cola.cola import Cola
from objects.TDA.arbol_binario import arbolBinario
from objects.TDA.arbol_nario import arbolNario

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

                        if amountInput == 3:
                            
                            listFolderUnit = arbolBinario.ArbolBinario
                            needFolderUnit = True

                            listFolderUnit = self.__validationCommands.validationUnit(needFolderUnit)

                            if listFolderUnit is not None:
                
                                nameFolder = "".join(args[1])
                    
                                self.__commands[comando].execute(amountInput, listFolderUnit, nameFolder)
                        
                            else:
                                print("Unidad no encontrada")
                        
                        if amountInput == 4:
                    
                            listFolderUnit = arbolBinario.ArbolBinario
                            needFolderUnit = True

                            listFolderUnit = self.__validationCommands.validationUnit(needFolderUnit)

                            if listFolderUnit is not None:

                                listSubFolder = arbolBinario.ArbolBinario
                                nameFolder = "".join(args[1])

                                listSubFolder = self.__validationCommands.validationFolder(listFolderUnit, nameFolder)

                                if listSubFolder is not None:
                                    nameFolder = "".join(args[2])
                                    self.__commands[comando].execute(amountInput, listSubFolder, nameFolder)
                                else:

                                    print("Subcarpeta no encontrada")
                            else:
                                print("Unidad no encontrada")


                    if comando == "type":

                        if amountInput == 3:
                            
                            correctArgs = False
                            correctArgs = self.__validationCommands.validationExtensionFile(args[0])
                            
                            if correctArgs:
                                value = args[0].split(".")
                                
                                nameFile = value[0]
                                extensionFile = value[1]
                                content = args[1]
                                newFile = file(None,nameFile,None, extensionFile,datetime.datetime.now,None,content)

                                self.__commands[comando].execute(self.__validationCommands.getSizeCommand(), newFile, self.__unit)  
                        
                        if amountInput == 6:

                            correctArgs = False
                            correctArgs = self.__validationCommands.validationExtensionFile(args[3])
                            
                            if correctArgs:
                                value = args[3].split(".")
                                nameFile = value[0]
                                extensionFile = value[1]
                                content = args[3]

                                newFile = file(None,nameFile,None, extensionFile,datetime.datetime.now,None,content)
                                
                                #Indicara al metodo que retorne la lista de carpetas de la unidad
                                needFolderUnit = True
                                #lista de carpetas de la  unidad a buscar 
                                listFolderUnit = arbolBinario.ArbolBinario()
                                listFolderUnit = self.__validationCommands.validationUnit(needFolderUnit)

                                if listFolderUnit is not None:
     
                                    listSubFolder = arbolBinario.ArbolBinario()
                                    listSubFolder =  self.__validationCommands.validationFolder(listFolderUnit, args[1])

                                    if listSubFolder is not None:
                                    
                                        #Comprueba si la subcarpeta ingresada es valida
                                        listFilesSubFolder = arbolNario.ArbolNArio()
                                        listFilesSubFolder =  self.__validationCommands.validationSubFolder(listSubFolder, args[2])
                                        
                                        if listFilesSubFolder is not None:
                                            
                                            self.__commands[comando].execute(self.__validationCommands.getSizeCommand(), newFile, listFilesSubFolder)
                                        
                                        else:
                                            
                                            print("Ingrese una subcarpeta valida")
                                    else:

                                        print("Ingrese una carpeta valida")
                                else:

                                    print("Unidad no encontrada")
                    
                    #EJECUTA EL COMANDO DIR
                    if comando == "dir":

                        for unit in self.__unit:
                            
                            self.__commands[comando].execute(unit)
                            break

                    #EJECUTA EL COMANDO CD
                    if comando == "cd":
                        
                        folder1 = folder

                        listFolderUnit = arbolBinario.ArbolBinario
                        needFolderUnit = True

                        listFolderUnit = self.__validationCommands.validationUnit(needFolderUnit)

                        if listFolderUnit is not None:

                            listSubFolder = arbolBinario.ArbolBinario
                            nameFolder = "".join(args[1])

                            listSubFolder = self.__validationCommands.validationFolder(listFolderUnit, nameFolder)

                            if listSubFolder is not None:

                                nameFolder = "".join(args[2])
                                folder1 = self.__validationCommands.validationSubFolderGetReference(listSubFolder,nameFolder)
                                
                                if folder1 is not None:

                                    listFiles = arbolNario
                                    listSub = arbolBinario

                                    listFiles = folder1.getFileListFolder()
                                    raizFiles = folder1.getFileListFolder().getRaiz()
                                    listSub = folder1.getFolderList()
                                
                                    self.__commands[comando].execute(listFiles, raizFiles, listSub)
                                
                                else:
                                    print("Subcarpeta no ecnontrada")
                            else:

                                print("Carpeta no encontrada")
                        else:
                            print("Unidad no encontrada")
                    
                    #EJECUTA EL COMANDO MKDIR
                    if comando == "mkdir":

                        needFolderUnit = False
                        
                        if amountInput == 2:

                            folder1 = folder(0,partes[1],None,None,None,None)
                            if folder1 is None and self.__unit is None:

                                print("Ingrese una ruta valida para crear una nueva carpeta")
                            
                            if folder1 is not None and self.__unit is not None:
                                
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