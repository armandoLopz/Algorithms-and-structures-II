from objects.userManage import user 
from objects.DOSconsolePA import DOSconsole as dc
from objects.SystemComponents import unit as unit_module
from uploadContent import upload

#Se crea el usuario que ejecutara los comandos en la consola
user = user.user
userCreate = False

while userCreate == False:

    try:

        userCreate, user = user.createUser()

    except:
        
        print("Verifique los datos ingresados")

#Objeto unidad con la que se va a trabajar en la carga de archivos
unit = unit_module.unit
#Carga de archivos 
uploadObjects = upload.upload(unit)

#Inicializacion de la DOSconsole
dosConsole = dc.DOSConsole(uploadObjects.createUnit(), user)
dosConsole.run()