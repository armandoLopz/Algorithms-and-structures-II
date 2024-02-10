import sys
import os
import json
import fichero 
import unidad 
import carpeta 
import comando 
import time
import user as us
import datetime

def createUser():

    userCreate = False
    print("Ingrese los siguientes datos")
    idUser = int(input("ID: "))
    nameUser = input("Nombre: ")
    lastNameUser = input("Apellido: ")
    cedulaUser = int(input("Cedula: "))
    rolUser = int(input("Ingrese su rol: \n1-INVITADO\n2-ADMINISTRADOR\n"))

    if rolUser == 1:

        userCreate = True
        usuario = us.user(idUser,nameUser,lastNameUser,cedulaUser, rol="invitado")

        return userCreate , usuario
    
    elif rolUser == 2: 
    
        userCreate = True
        return userCreate, us.user(idUser,nameUser,lastNameUser,cedulaUser, rol="invitado")
    
    else:
        return userCreate, None
      
#Creacion del usuario

userCreate = False
user = ()

while userCreate == False:

    try:
        userCreate, user = createUser()
    
    except:
        
        print("Verifique los datos ingresados e inténtelo nuevamente")

#CARGA DE ARCHIVOS
with open('Parcial3\prueba.json', 'r') as archivo:

            #Se obtiene la ruta y size del archivo JSON para definir su valor
            fileRoute = "Parcial3\prueba.json"
            sizeFileBytes = os.path.getsize(fileRoute)
            SizeFileToKB = sizeFileBytes / 1024

            #Identificar el nombre y la extension del archivo

            nameFile, extensionFile = os.path.splitext(fileRoute)

            datosJson = json.load(archivo)

            #Se define el valor del size del JSON 
            datosJson["archivo1"]["size"] = SizeFileToKB
            #Se define el valor de la extension del archivo
            datosJson["archivo1"]["extension"] = extensionFile

with open('Parcial3\prueba2.json', 'r') as archivo:

            #Se obtiene la ruta y size del archivo JSON para definir su valor
            sizeFileBytes = os.path.getsize("Parcial3\prueba2.json")
            SizeFileToKB = sizeFileBytes / 1024

            datosJson2 = json.load(archivo)

            #Se define el valor del size del JSON 
            datosJson2["archivo2"]["size"] = SizeFileToKB
            #Se define el valor de la extension del archivo
            datosJson2["archivo2"]["extension"] = extensionFile

with open('Parcial3\prueba3.json', 'r') as archivo:

            #Se obtiene la ruta y size del archivo JSON para definir su valor
            sizeFileBytes = os.path.getsize("Parcial3\prueba3.json")
            SizeFileToKB = sizeFileBytes / 1024

            datosJson3 = json.load(archivo)

            #Se define el valor del JSON 
            datosJson3["archivo3"]["size"] = SizeFileToKB
            #Se define el valor de la extension del archivo
            datosJson3["archivo3"]["extension"] = extensionFile

with open('Parcial3\prueba4.json', 'r') as archivo:

            #Se obtiene la ruta y size del archivo JSON para definir su valor
            sizeFileBytes = os.path.getsize("Parcial3\prueba4.json")
            SizeFileToKB = sizeFileBytes / 1024

            datosJson4 = json.load(archivo)

            #Se define el valor del size del JSON 
            datosJson4["archivo4"]["size"] = SizeFileToKB
            #Se define el valor de la extension del archivo
            datosJson4["archivo4"]["extension"] = extensionFile

with open('Parcial3\prueba5.json', 'r') as archivo:

            #Se obtiene la ruta y size del archivo JSON para definir su valor
            sizeFileBytes = os.path.getsize("Parcial3\prueba5.json")
            SizeFileToKB = sizeFileBytes / 1024

            datosJson5 = json.load(archivo)

            #Se define el valor del size del JSON 
            datosJson5["archivo5"]["size"] = SizeFileToKB
            #Se define el valor de la extension del archivo
            datosJson5["archivo5"]["extension"] = extensionFile

#Instaciacion de los objetos de tipo fichero
            
file1 = fichero.fichero(datosJson["archivo1"]["id"], datosJson["archivo1"]["name"], datosJson["archivo1"]["size"], datosJson["archivo1"]["extension"], datosJson["archivo1"]["creationDate"],datosJson["archivo1"]["content"], datosJson["archivo1"]["modificationDate"])
file2 = fichero.fichero(datosJson2["archivo2"]["id"], datosJson2["archivo2"]["name"], datosJson2["archivo2"]["size"], datosJson2["archivo2"]["extension"], datosJson2["archivo2"]["creationDate"],datosJson2["archivo2"]["content"], datosJson2["archivo2"]["modificationDate"])
file3 = fichero.fichero(datosJson3["archivo3"]["id"], datosJson3["archivo3"]["name"], datosJson3["archivo3"]["size"], datosJson3["archivo3"]["extension"], datosJson3["archivo3"]["creationDate"],datosJson3["archivo3"]["content"], datosJson3["archivo3"]["modificationDate"])
file4 = fichero.fichero(datosJson4["archivo4"]["id"], datosJson4["archivo4"]["name"], datosJson4["archivo4"]["size"], datosJson4["archivo4"]["extension"], datosJson4["archivo4"]["creationDate"],datosJson4["archivo4"]["content"], datosJson4["archivo4"]["modificationDate"])
file5 = fichero.fichero(datosJson5["archivo5"]["id"], datosJson5["archivo5"]["name"], datosJson5["archivo5"]["size"], datosJson5["archivo5"]["extension"], datosJson5["archivo5"]["creationDate"],datosJson5["archivo5"]["content"], datosJson5["archivo5"]["modificationDate"])

#Instaciacion de la lista con los ficheros
listFiles = [file1, file2, file3, file4, file5]

ca = carpeta.carpeta(1,"Archivos JSON", 400, datetime.datetime.now, listFiles, None)
ca2 = carpeta.carpeta(2,"Imagenes Familia", 300, datetime.datetime.now, listFiles, None)
ca3 = carpeta.carpeta(3,"Contenido PDF", 1400, datetime.datetime.now, listFiles, None)

listFolders = [ca,ca2,ca3]

#Creación de la Unidad de Almacenamiento
un1 = unidad.unidad(1,"C",1024, 350, "SSD", listFolders)

#Creación del comando dir
comando1 = comando.comando(1,"comando dir", "Describe los archivos que hay en la unidad ", "ADMINISTRADOR")

#QUICKSORT

#ORDEN ASCENDENTE
def partitionasc(arr, low, high):
    i = low - 1
    pivot = arr[high][1]
    
    for j in range(low, high):
        if arr[j][1] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quicksortasc(arr, low, high):
    if low < high:
        pi = partitionasc(arr, low, high)
        quicksortasc(arr, low, pi-1)
        quicksortasc(arr, pi+1, high)


#ORDEN DESCENDENTE
def partitiondesc(arr, low, high):
    i = low - 1
    pivot = arr[high][1]
    
    for j in range(low, high):
        if arr[j][1] >= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quicksortdesc(arr, low, high):
    if low < high:
        pi = partitiondesc(arr, low, high)
        quicksortdesc(arr, low, pi-1)
        quicksortdesc(arr, pi+1, high)

# Directorio donde se encuentran los archivos JSON
directorio = 'Parcial3'

# Obtener la lista de archivos JSON en el directorio
archivos_json1 = [(archivo, os.path.getsize(os.path.join(directorio, archivo))) for archivo in os.listdir(directorio) if archivo.endswith('.json')]
archivos_json2 = [(archivo, os.path.getsize(os.path.join(directorio, archivo))) for archivo in os.listdir(directorio) if archivo.endswith('.json')]


# Ordenar la lista de archivos por tamaño utilizando Quicksort
quicksortasc(archivos_json1, 0, len(archivos_json1)-1)
quicksortdesc(archivos_json2, 0, len(archivos_json2)-1)


#ORDENAR ARCHIVOS POR FECHA DE CREACIÓN CON QUICKSORT

archivos_json3 = [(archivo, os.path.getctime(os.path.join(directorio, archivo))) for archivo in os.listdir(directorio) if archivo.endswith('.json')]
archivos_json4 = [(archivo, os.path.getctime(os.path.join(directorio, archivo))) for archivo in os.listdir(directorio) if archivo.endswith('.json')]

# Ordenar la lista de archivos por fecha de creación utilizando Quicksort
quicksortasc(archivos_json3, 0, len(archivos_json3)-1)
quicksortdesc(archivos_json4, 0, len(archivos_json4)-1)

#MERGESORT
#ORDEN ASCENDENTE
def merge_sortasc(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left = merge_sortasc(left)
    right = merge_sortasc(right)
    
    return mergeasc(left, right)

def mergeasc(left, right):
    merged = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i][1] < right[j][1]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    while i < len(left):
        merged.append(left[i])
        i += 1
    
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged

#ORDEN DESCENDENTE
def merge_sortdesc(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left = merge_sortdesc(left)
    right = merge_sortdesc(right)
    
    return mergedesc(left, right)

def mergedesc(left, right):
    merged = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i][1] > right[j][1]:  
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    while i < len(left):
        merged.append(left[i])
        i += 1
    
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged

# Directorio donde se encuentran los archivos JSON
directorio = 'Parcial3'

# Obtener la lista de archivos JSON en el directorio con sus fechas de modificación
archivos_json1 = [(archivo, os.path.getmtime(os.path.join(directorio, archivo))) for archivo in os.listdir(directorio) if archivo.endswith('.json')]
archivos_json2 = [(archivo, os.path.getmtime(os.path.join(directorio, archivo))) for archivo in os.listdir(directorio) if archivo.endswith('.json')]

# Ordenar la lista de archivos por fecha de modificación utilizando Mergesort
archivos_json1 = merge_sortasc(archivos_json1)
archivos_json2 = merge_sortdesc(archivos_json2)

#EJECUCIÓN DE LOS COMANDOS
#Clase comando del cual todos los comandos heredan
class Command:
    def execute(self, args):
        raise NotImplementedError("Debe implementar este método")

class DirCommand(Command):
#El metodo execute sirve para ejecutar toda la accion que hace el 
#comando al ser llamado desde la consola
    def execute(self, args):
        print("Listando archivos en el directorio actual...")
        print(comando1.commandDir(un1))

#Comando para ordenar archivos en orden ascendente, teniendo como criterio su tamaño
class AscCommand(Command):
    def execute(self, args):
        print("Listando archivos en el directorio actual...")
        print("ORDEN ASCENDENTE - TAMAÑO DEL ARCHIVO")
        for archivo, tamaño in archivos_json1:
            print(f'{archivo}: {tamaño} bytes')
            print("")
        print("\n")

#Comando para ordenar archivos en orden descendente, teniendo como criterio su tamaño
class DescCommand(Command):
     def execute(self, args):
        print("Listando archivos en el directorio actual...")
        print("ORDEN DESCENDENTE - TAMAÑO DEL ARCHIVO")
        for archivo, tamaño in archivos_json2:
            print(f'{archivo}: {tamaño} bytes')
            print("")
        print("\n")

#Comando que lista a los archivos por fecha de modificación, del menos reciente al más reciente
class ModificacionAscCommand(Command):
     def execute(self, args):
        print("Listando archivos en el directorio actual...")
        print("ORDEN ASCENDENTE - FECHA DE MODIFICACIÓN DEL ARCHIVO")
        for archivo, fecha_modificacion in archivos_json1:
            fecha_formateada = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(fecha_modificacion))
            print(f'{archivo}: {fecha_formateada}')
            print("")
        print("\n")

#Comando que lista a los archivos por fecha de modificación, del más reciente al menos reciente
class ModificacionDescCommand(Command):
     def execute(self,args):
        print("Listando archivos en el directorio actual...")
        print("ORDEN DESCENDENTE - FECHA DE MODIFICACIÓN DEL ARCHIVO")
        for archivo, fecha_modificacion in archivos_json2:
            fecha_formateada = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(fecha_modificacion))
            print(f'{archivo}: {fecha_formateada}')
            print("")
        print("\n")

#Comando que lista a los archivos por fecha de creación, del menos reciente al más reciente
class CreacionAscCommand(Command):
    def execute(self, args):
        print("Listando archivos en el directorio actual...")
        print("ORDEN ASCENDENTE - FECHA DE CREACIÓN DEL ARCHIVO")
        for archivo, fecha_creacion in archivos_json3:
            fecha_formateada = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(fecha_creacion))
            print(f'{archivo}: {fecha_formateada}')
            print("")
        print("\n") 

#Comando que lista a los archivos por fecha de creación, del más reciente al menos reciente
class CreacionDescCommand(Command):
     def execute(self, args):
        print("Listando archivos en el directorio actual...")
        print("ORDEN DESCENDENTE - FECHA DE CREACIÓN DEL ARCHIVO")
        for archivo, fecha_creacion in archivos_json4:
            fecha_formateada = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(fecha_creacion))
            print(f'{archivo}: {fecha_formateada}')
            print("")
        print("\n") 

#Comando para mostrar en pantalla
class EchoCommand(Command):
    def execute(self, args):
        if args:
            print(" ".join(args))
        else:
            print("Error: 'echo' necesita un parámetro.")


#Comando para salir de la consola
class ExitCommand(Command):
    def execute(self, args):
        print("Saliendo...")
        sys.exit()


#Ejemplo de comando ayuda
class HelpCommand(Command):
    def execute(self, args):
        print("Comandos disponibles:")
        print("dir - Lista los archivos en el directorio actual")
        print("echo [mensaje] - Repite el mensaje")
        print("exit - Sale de la consola")
        print("help - Muestra esta ayuda")
        print("asc - Lista los archivos por orden de tamaño, de menor a mayor")
        print("desc - Lista los archivos por orden de tamaño, de mayor a menor")
        print("modasc - Lista los archivos por fecha de modificación, del menos reciente al más reciente")
        print("modesc - Lista los archivos por fecha de modificación, del más reciente al menos reciente")
        print("creasc - Lista a los archivos por fecha de creación, del menos reciente al meás reciente")
        print("credesc - lista a los archivos por fecha de creación, del más reciente al menos reciente ")
        print("\n") 


#clase principal
class DOSConsole:
    def __init__(self):

#Lista de comados disponibles, cuando se agregue un nuevo comando, se carga e esta lista
        self.commands = {
        "dir": DirCommand(),
        "echo": EchoCommand(),
        "exit": ExitCommand(),
        "help": HelpCommand(),
        "asc" : AscCommand(),
        "desc": DescCommand(),
        "modasc": ModificacionAscCommand(),
        "modesc": ModificacionDescCommand(),
        "creasc": CreacionAscCommand(),
        "credesc": CreacionDescCommand()

        }
#El metodo run se utiliza para correr la consola e iniciar el programa
    def run(self):
        while True:
            try:
    #C: Es la unidad actual
                entrada = input("C:\\> ")
                partes = entrada.split()
                comando = partes[0].lower() if partes else None
                args = partes[1:]

    #Se busca si el comando existe en la lista definida previamente
                if comando in self.commands:
    #Si el comando existe se llama en la lista definida anteriormente
    #la lista es un diccionario donde cada clave corresponde a un comando
    #y cada valor de ese diccionario es un objeto del comando
    #después se llama execute de ese objeto para ejecutar el comando
                    self.commands[comando].execute(args)
                    
                else:
                    print(f"Comando desconocido: {comando}")
            except KeyboardInterrupt:
                print("\nOperación cancelada por el usuario.")
                break
            except Exception as e:
                print(f"Error: {e}")

consola = DOSConsole()
consola.run()