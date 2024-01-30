import fichero 
import unidad 
import carpeta 
import comando 
import datetime
import json
import os


with open('Parcial3\prueba.json', 'r') as archivo:

    #fileRoute = "Parcial3\prueba.json"
    sizeFileBytes = os.path.getsize("Parcial3\prueba.json")

    datosJson = json.load(archivo)

with open('Parcial3\prueba2.json', 'r') as archivo:

    fileRoute = "Parcial3\prueba2.json"
    datosJson2 = json.load(archivo)

file1 = fichero.fichero(datosJson.get("id"), datosJson.get("name"), datosJson.get("size"), datosJson.get("extension"), datosJson.get("creationDate"), datosJson.get("content"), datosJson.get("modificationDate"))
file2 = fichero.fichero(datosJson2.get("id"), datosJson2.get("name"), datosJson2.get("size"), datosJson2.get("extension"), datosJson2.get("creationDate"), datosJson2.get("content"), datosJson2.get("modificationDate"))
#file1 = fichero.fichero(datosJson["archivo1"]["id"], datosJson["archivo1"]["name"], datosJson["archivo1"]["size"], datosJson["archivo1"]["extension"], datosJson["archivo1"]["creationDate"],datosJson["archivo1"]["content"], datosJson["archivo1"]["modificationDate"])
#file2 = fichero.fichero(datosJson["archivo2"]["id"], datosJson["archivo2"]["name"], datosJson["archivo2"]["size"], datosJson["archivo2"]["extension"], datosJson["archivo2"]["creationDate"],datosJson["archivo2"]["content"], datosJson["archivo2"]["modificationDate"])
#file3 = fichero.fichero(datosJson["archivo3"]["id"], datosJson["archivo3"]["name"], datosJson["archivo3"]["size"], datosJson["archivo3"]["extension"], datosJson["archivo3"]["creationDate"],datosJson["archivo3"]["content"], datosJson["archivo3"]["modificationDate"])
#file4 = fichero.fichero(datosJson["archivo4"]["id"], datosJson["archivo4"]["name"], datosJson["archivo4"]["size"], datosJson["archivo4"]["extension"], datosJson["archivo4"]["creationDate"],datosJson["archivo4"]["content"], datosJson["archivo4"]["modificationDate"])
#file5 = fichero.fichero(datosJson["archivo"]["id"], datosJson["archivo"]["name"], datosJson["archivo"]["size"], datosJson["archivo5"]["extension"], datosJson["archivo5"]["creationDate"],datosJson["archivo5"]["content"], datosJson["archivo5"]["modificationDate"])

fi = fichero.fichero(1,"Documentos",20,".json", 20, "Archivo de prueba" )
fi1 = fichero.fichero(2,"archivos futbol",70,".json", 120, "Archivo de prueba" )
fi2 = fichero.fichero(3,"archivos beisbol",270,".json", 220, "Archivo de prueba" )
fi3 = fichero.fichero(4,"archivos tenis",40,".json", 204, "Archivo de prueba" )

listFiles = [fi,fi1,fi2,fi3]

ca = carpeta.carpeta(1,"Imagenes", 400, datetime.datetime.now, listFiles, None)
ca2 = carpeta.carpeta(2,"Imagenes Familia", 300, datetime.datetime.now, listFiles, None)
ca3 = carpeta.carpeta(3,"Contenido PDF", 1400, datetime.datetime.now, listFiles, None)

listFolders = [ca,ca2,ca3]

un1 = unidad.unidad(1,"C",1024, 350, "SSD", listFolders)

#print(fi.showDetailsFile())
#print("ARCHIVOS DE LA CARPETA: ")
#print(ca.contentFolder())

comando = comando.comando(1,"comando dir", "Describe los archivos que hay en la unidad ", "ADMIN")

print("COMANDO DIR ")

#print(comando.commandDir(un1))

#ficheroJson2 = fichero.fichero(datosJson.get(['archivo2']['id']), datosJson.get(['archivo2']['name']),datosJson.get(['archivo2']['size']),datosJson.get(['archivo2']['extension']), datosJson.get(['archivo2']['creationDate']), datosJson.get(['archivo2']['modificationDate']), datosJson.get(['archivo2']['content']))

print("DATOS 1ER ARCHIVO: ")
print(file1.showDetailsFile())
print("")
print("DATOS 2DO ARCHIVO: ")
#print(file2.showDetailsFile())