class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def getName(self):

        return self.nombre

class Pila:
    def __init__(self):
        self.tope = None
    
    def esta_vacia(self):
        return self.tope is None
    
    def agregar(self, valor):
        nodo_nuevo = Nodo(valor)
        nodo_nuevo.siguiente = self.tope
        self.tope = nodo_nuevo

    def eliminar(self):
        if self.esta_vacia():
            return None
        else:
            valor_eliminado = self.tope.valor
            self.tope = self.tope.siguiente
            return valor_eliminado
        
    def ver_tope(self):
        if self.esta_vacia():
            return None
        else:
            return self.tope.valor
    
    def obtener_objetos(self):
        objetos = []
        nodo_actual = self.tope
        while nodo_actual is not None:
            objetos.append(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente
        return objetos

    def recorrer(self):
        if self.esta_vacia():
            print("La pila está vacía")
        else:
            self._recorrer_aux(self.tope)

    def _recorrer_aux(self, nodo):
        valores = []
        while nodo is not None:
            valores.append(nodo.valor)
            nodo = nodo.siguiente
        return valores

# Creamos algunas mascotas
mascota1 = Mascota("Luna", "Perro", 3)
mascota2 = Mascota("Simba", "Gato", 5)
mascota3 = Mascota("Bolt", "Perro", 2)
mascota3 = Mascota("Ares", "Perro", 2)
# Creamos una pila y agregamos las mascotas a la pila
pila_mascotas = Pila()

pila_mascotas.agregar(mascota1)
pila_mascotas.agregar(mascota2)
pila_mascotas.agregar(mascota3)

# Imprimimos todas las mascotas en la pila
pila_mascotas.recorrer()

print(pila_mascotas.esta_vacia())

list = pila_mascotas.obtener_objetos()
print(list.__len__())

for Mascota in list:

    print(Mascota.getName())