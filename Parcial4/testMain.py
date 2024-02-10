from objects.userManage import user 
from objects.DOSconsolePA import DOSconsole as dc
from objects.SystemComponents import unit as unit_module
from objects.SystemComponents import folder as fl
from uploadContent import upload

#Se crea el usuario que ejecutara los comandos en la consola

user = user.user
userCreate = False

while userCreate == False:

    try:

        userCreate, user = user.createUser()

    except:
        
        print("Verifique los datos ingresados")

#Carga de archivos 
unit = unit_module.unit
uploadObjects = upload.upload(unit)

print(unit.getNameUnit())

uploadObjects.datosJson()
uploadObjects.createFiles()
folders = uploadObjects.createFolder()

#Inicializacion de la DOSconsole
dosConsole = dc.DOSConsole(uploadObjects.createUnit(), userCreate)