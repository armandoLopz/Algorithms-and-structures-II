from objects.TDA.Pila import pila as pl
from objects.TDA.LinkedList import LinkedList as ll
import objeto as ob

pila = pl.Pila()
LinkedList = ll.ListaEnlazada()

object = ob.objeto(1)
object2 = ob.objeto(14)
object3 = ob.objeto(4)
object4 = ob.objeto(5)
object5 = ob.objeto(6)
object6 = ob.objeto(7)
object7 = ob.objeto(8)
object8 = ob.objeto(9)
object9 = ob.objeto(10)

LinkedList.agregar(object)
LinkedList.agregar(object2)
LinkedList.agregar(object3)
LinkedList.agregar(object4)
LinkedList.agregar(object5)
LinkedList.agregar(object6)
LinkedList.agregar(object7)
LinkedList.agregar(object8)
LinkedList.agregar(object9)

lista = ll.ListaEnlazada()

lista.agregar(object)


print(list(lista))


lista.insertar(0, object2)
print(list(lista))

lista.agregar(object3)
lista.agregar(object5)
lista.agregar(object7)
lista.agregar(object8)
lista.agregar(object9)

print(lista.obtener(3))

print(lista.index(object8))

print("La longitud de la lista es " , lista.__len__())

print("Iteracion de la lista es " ,  lista.__iter__())
