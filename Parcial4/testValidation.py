from objects.DOSconsolePA.validationCommands import validationCommands
from objects.SystemComponents.unit import unit
from uploadContent.upload import upload

exe = validationCommands

unidad = unit

uploadObjects = upload(unidad)
name = input("Nombre del comando")
args = input("Argumentos del comando")

exe(uploadObjects.createUnit(), name,None,args.split())



