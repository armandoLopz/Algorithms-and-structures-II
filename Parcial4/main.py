from objects.userManage import user 
from objects.DOSconsolePA import DOSconsole as dc
from objects.SystemComponents import unit as unit_module
from uploadContent import uploadListUnits

#Se crea el usuario que ejecutara los comandos en la consola
user = user.user
userCreate = False
"""
while userCreate == False:

    try:

        userCreate, user = user.createUser()

    except:
        
        print("Verifique los datos ingresados")"""

#Carga de los archivos que tendran las unidades 
carga = []
carga = uploadListUnits.CreateLinkedListUnit()

#Inicializacion de la DOSconsole
dosConsole = dc.DOSConsole(carga, user)
dosConsole.run()