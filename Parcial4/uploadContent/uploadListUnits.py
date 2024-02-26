from objects.SystemComponents.unit import unit
from . import upload 
from . import upload2
from . import upload3
from objects.TDA.LinkedList.linkedList import ListaEnlazada

def CreateLinkedListUnit():

    unitC = unit
    unitD = unit
    unitF = unit

    linkedList = ListaEnlazada()

    uploadC = upload.upload(unitC)
    uploadD = upload2.upload(unitD)
    uploadF = upload3.upload(unitF)

    linkedList.agregar(uploadC.createUnit())
    linkedList.agregar(uploadD.createUnit())
    linkedList.agregar(uploadF.createUnit())

    return linkedList

