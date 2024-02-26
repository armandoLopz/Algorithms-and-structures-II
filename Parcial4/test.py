from uploadContent.upload2 import upload
from objects.SystemComponents.unit import unit
from uploadContent import uploadListUnits

unidad = unit
carga = []
carga = uploadListUnits.CreateLinkedListUnit()
print(carga)
for unit in carga:

    if "contactos" in unit.getFolderList().preorden():
        print("SE ENCUENTRA ADENTRO")
    print("")

