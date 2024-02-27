from uploadContent.upload import upload
from objects.SystemComponents.unit import unit
from uploadContent import uploadListUnits

unidad = unit
carga = []
#carga = uploadListUnits.CreateLinkedListUnit()
#print(carga)
"""for unit in carga:

    if "contactos" in unit.getFolderList().preorden():
        print("SE ENCUENTRA ADENTRO")
    print("")"""


cargaC = upload(unit)

cargaC.createFilesJson()