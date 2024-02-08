import archivosJSON
import algortimos
import os
import json
import fichero 
import unidad 
import carpeta 
import comando 
import user as us
import time
import datetime

def createUser():

    userCreate = False

    idUser = int(input("ID: "))
    nameUser = input("Nombre: ")
    lastNameUser = input("Apellido: ")
    cedulaUser = int(input("Cedula: "))
    rolUser = int(input("Ingrese su rol: \n1-INVITADO\n2-ADMINISTRADOR"))

    if rolUser == 1:

        userCreate = True
        usuario = us.user(idUser,nameUser,lastNameUser,cedulaUser, rol="invitado")

        return userCreate , usuario
    
    elif rolUser == 2: 
    
        userCreate = True
        return userCreate, us.user(idUser,nameUser,lastNameUser,cedulaUser, rol="invitado")
    else:
        print("Verifique los datos e ingreselos correctamente")
        return userCreate, None
      
#Creacion del usuario

userCreate = False
user = ()

print("Ingrese los siguientes datos")

while userCreate == False:

    try:
        userCreate, user = createUser()
    
    except:
        print("Verifique los datos ingresados e ingreselos correctamente")

#CARGA DE ARCHIVOS
with open('Parcial3 copy\Archivo1.json', 'r') as archivo:

            #Se obtiene la ruta y size del archivo JSON para definir su valor
            fileRoute = "Parcial3 copy\Archivo1.json"
            sizeFileBytes = os.path.getsize(fileRoute)
            SizeFileToKB = sizeFileBytes / 1024

            #Identificar el nombre y la extension del archivo

            nameFile, extensionFile = os.path.splitext(fileRoute)

            datosJson = json.load(archivo)

            #Se define el valor del size del JSON 
            datosJson["archivo1"]["size"] = SizeFileToKB
            #Se define el valor de la extension del archivo
            datosJson["archivo1"]["extension"] = extensionFile

with open('Parcial3 copy\Archivo2.json', 'r') as archivo:

            #Se obtiene la ruta y size del archivo JSON para definir su valor
            sizeFileBytes = os.path.getsize("Parcial3 copy\Archivo2.json")
            SizeFileToKB = sizeFileBytes / 1024

            datosJson2 = json.load(archivo)

            #Se define el valor del size del JSON 
            datosJson2["archivo2"]["size"] = SizeFileToKB
            #Se define el valor de la extension del archivo
            datosJson2["archivo2"]["extension"] = extensionFile

with open('Parcial3 copy\Archivo3.json', 'r') as archivo:

            #Se obtiene la ruta y size del archivo JSON para definir su valor
            sizeFileBytes = os.path.getsize("Parcial3 copy\Archivo3.json")
            SizeFileToKB = sizeFileBytes / 1024

            datosJson3 = json.load(archivo)

            #Se define el valor del JSON 
            datosJson3["archivo3"]["size"] = SizeFileToKB
            #Se define el valor de la extension del archivo
            datosJson3["archivo3"]["extension"] = extensionFile

with open('Parcial3 copy\Archivo4.json', 'r') as archivo:

            #Se obtiene la ruta y size del archivo JSON para definir su valor
            sizeFileBytes = os.path.getsize("Parcial3 copy\Archivo4.json")
            SizeFileToKB = sizeFileBytes / 1024

            datosJson4 = json.load(archivo)

            #Se define el valor del size del JSON 
            datosJson4["archivo4"]["size"] = SizeFileToKB
            #Se define el valor de la extension del archivo
            datosJson4["archivo4"]["extension"] = extensionFile

with open('Parcial3 copy\Archivo5.json', 'r') as archivo:

            #Se obtiene la ruta y size del archivo JSON para definir su valor
            sizeFileBytes = os.path.getsize("Parcial3 copy\Archivo5.json")
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

#Instanciacion del objeto de algoritmos

algoritmo = algortimos.algoritmos()

# Directorio donde se encuentran los archivos JSON
directorio = 'Parcial3 copy'

# Obtener la lista de archivos JSON en el directorio
archivos_json1 = [(archivo, os.path.getsize(os.path.join(directorio, archivo))) for archivo in os.listdir(directorio) if archivo.endswith('.json')]
archivos_json2 = [(archivo, os.path.getsize(os.path.join(directorio, archivo))) for archivo in os.listdir(directorio) if archivo.endswith('.json')]

# Ordenar la lista de archivos por tamaño utilizando Quicksort
algoritmo.quicksortasc(archivos_json1 , 0 , len(archivos_json1)-1)
algoritmo.quicksortdesc(archivos_json2 , 0, len(archivos_json2)-1)
#algoritmo.quicksortasc(archivos_json1, 0, len(archivos_json1)-1)
#algoritmo.quicksortdesc(archivos_json2, 0, len(archivos_json2)-1)

#ORDENAR ARCHIVOS POR FECHA DE CREACIÓN CON QUICKSORT

archivos_json3 = [(archivo, os.path.getctime(os.path.join(directorio, archivo))) for archivo in os.listdir(directorio) if archivo.endswith('.json')]
archivos_json4 = [(archivo, os.path.getctime(os.path.join(directorio, archivo))) for archivo in os.listdir(directorio) if archivo.endswith('.json')]

# Ordenar la lista de archivos por fecha de creación utilizando Quicksort
algortimos.algoritmos.quicksortasc(archivos_json3, 0, len(archivos_json3)-1)
algortimos.algoritmos.quicksortdesc(archivos_json4, 0, len(archivos_json4)-1)

consola = DOSconsola.DOSConsole(comando1, un1, archivos_json1, archivos_json2 ,archivos_json3, archivos_json4)

consola.run()