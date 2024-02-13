from . import listCommand, validationCommands
class DOSConsole:

    def __init__(self, unit, user):

        self.__validationCommands = validationCommands.validationCommands()
        self.__unit = unit
        self.__commands = listCommand

    #lista de comados disponibles, cuando se agregue un nuevo comando, se carga e esta
        self.__commands = {
            
        "dir": self.__commands.DirCommand,
        "exit": self.__commands.ExitCommand,
        "help": self.__commands.HelpCommand,
        "cd": self.__commands.Cd
        
        }

#El metodo run se utiliza para correr la consola e iniciar el programa
    def run(self):
        while True:
            try:
    #C: Es la unidad actual
                entrada = input("C:\\> ")
                partes = entrada.split()
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
                    
                    if comando == "dir":

                        self.__commands[comando].execute(self.__unit)
                        
                    if comando == "cd":
                        
                        if self.__validationCommands.methodExecute():
                            
                            self.__commands[comando].execute()
                    #self.__commands[comando].execute(self.__unit)
        #Si el comando existe se llama en la lista definida anteriormente
        #la lista es un diccionario donde cada clave corresponde a un comando
        #y cada valor de ese diccionario es un objeto del comando
        #después se llama execute de ese objeto para ejecutar el comando
                        
                else:
                    print(f"Comando desconocido: {comando}")

            except KeyboardInterrupt:
                    print("\nOperación cancelada por el usuario.")
                    break
            #except Exception as e:
                    #print(f"Error: {e}")