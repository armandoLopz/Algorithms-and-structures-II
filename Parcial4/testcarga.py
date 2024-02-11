import json
import os 
from Parcial4.uploadContent import r
from objects.SystemComponents import file

pathFile = r"Parcial4\contFiles\archivo.json"

def datosJson():
    with open(pathFile, 'r') as archivo:

        datosJson = json.load(archivo)

        return datosJson
    
datosJso = datosJson


file1 = file.file(datosJso()["archivo1"]["id"], datosJso()["archivo1"]["name"], datosJso()["archivo1"]["size"], datosJso()["archivo1"]["extension"], datosJso()["archivo1"]["creationDate"],datosJso()["archivo1"]["content"], datosJso()["archivo1"]["modificationDate"])
file2 = file.file(datosJso()["archivo2"]["id"], datosJso()["archivo2"]["name"], datosJso()["archivo2"]["size"], datosJso()["archivo2"]["extension"], datosJso()["archivo2"]["creationDate"],datosJso()["archivo2"]["content"], datosJso()["archivo2"]["modificationDate"])

#print(datosJso()())
        
#size = os.path.getsize('Parcial4\fileUpload\archivo.json')

print("IMPRESION DE LOS DATOS DEL ARCHIVO CARGADOS DEL JSON")

print(file1.showDetailsFile())

print(file2.showDetailsFile())