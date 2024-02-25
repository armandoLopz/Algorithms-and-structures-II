from uploadContent.upload2 import upload
from objects.SystemComponents.unit import unit
from uploadContent import uploadListUnits

unidad = unit
carga = []
carga = uploadListUnits.CreateLinkedListUnit()
print(carga)
for unit in carga:

    print(unit.getNameUnit())