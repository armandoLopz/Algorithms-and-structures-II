import fichero 
import unidad 
import carpeta 
import comando 
import datetime
import json
import os

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

file1 = fichero.fichero(datosJson["archivo1"]["id"], datosJson["archivo1"]["name"], datosJson["archivo1"]["size"], datosJson["archivo1"]["extension"], datosJson["archivo1"]["creationDate"],datosJson["archivo1"]["content"], datosJson["archivo1"]["modificationDate"])
file2 = fichero.fichero(datosJson2["archivo2"]["id"], datosJson2["archivo2"]["name"], datosJson2["archivo2"]["size"], datosJson2["archivo2"]["extension"], datosJson2["archivo2"]["creationDate"],datosJson2["archivo2"]["content"], datosJson2["archivo2"]["modificationDate"])
file3 = fichero.fichero(datosJson3["archivo3"]["id"], datosJson3["archivo3"]["name"], datosJson3["archivo3"]["size"], datosJson3["archivo3"]["extension"], datosJson3["archivo3"]["creationDate"],datosJson3["archivo3"]["content"], datosJson3["archivo3"]["modificationDate"])
file4 = fichero.fichero(datosJson4["archivo4"]["id"], datosJson4["archivo4"]["name"], datosJson4["archivo4"]["size"], datosJson4["archivo4"]["extension"], datosJson4["archivo4"]["creationDate"],datosJson4["archivo4"]["content"], datosJson4["archivo4"]["modificationDate"])
file5 = fichero.fichero(datosJson5["archivo5"]["id"], datosJson5["archivo5"]["name"], datosJson5["archivo5"]["size"], datosJson5["archivo5"]["extension"], datosJson5["archivo5"]["creationDate"],datosJson5["archivo5"]["content"], datosJson5["archivo5"]["modificationDate"])

listFiles = [file1, file2, file3, file4, file5]

ca = carpeta.carpeta(1,"Archivos JSON", 400, datetime.datetime.now, listFiles, None)
ca2 = carpeta.carpeta(2,"Imagenes Familia", 300, datetime.datetime.now, listFiles, None)
ca3 = carpeta.carpeta(3,"Contenido PDF", 1400, datetime.datetime.now, listFiles, None)

listFolders = [ca,ca2,ca3]

un1 = unidad.unidad(1,"C",1024, 350, "SSD", listFolders)

#print(fi.showDetailsFile())
#print("ARCHIVOS DE LA CARPETA: ")
#print(ca.contentFolder())

#comando = comando.comando(1,"comando dir", "Describe los archivos que hay en la unidad ", "ADMIN")

#print("COMANDO DIR ")

#print(comando.commandDir(un1))

#ficheroJson2 = fichero.fichero(datosJson.get(['archivo2']['id']), datosJson.get(['archivo2']['name']),datosJson.get(['archivo2']['size']),datosJson.get(['archivo2']['extension']), datosJson.get(['archivo2']['creationDate']), datosJson.get(['archivo2']['modificationDate']), datosJson.get(['archivo2']['content']))

print("DATOS 1ER ARCHIVO: ")
print(file1.showDetailsFile())
print("")
print("DATOS 2DO ARCHIVO: ")
print(file2.showDetailsFile())