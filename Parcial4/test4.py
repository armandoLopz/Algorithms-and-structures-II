class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Cola:

    def __init__(self):
        self.frente = None
        self.fin = None

    def esta_vacia(self):
        return self.frente is None
    
    def agregar(self, valor):
        nodo_nuevo = Nodo(valor)

        if self.esta_vacia():
            self.frente = nodo_nuevo

        else:
            self.fin.siguiente = nodo_nuevo
        self.fin = nodo_nuevo
            
    def eliminar(self):
        if self.esta_vacia():
            return None
        else:
            valor_eliminado = self.frente.valor
            self.frente = self.frente.siguiente
            
            if self.frente is None:
                self.fin = None
            return valor_eliminado
        
    def ver_frente(self):
        
        if self.esta_vacia():
            return None
        else:
            return self.frente.valor
        
    def recorrer(self):
        if self.esta_vacia():
            print("La cola está vacía")
        else:
            self._recorrer_aux(self.frente)

    def _recorrer_aux(self, nodo):
        if nodo is not None:
            
            print(nodo.valor.getName())
            self._recorrer_aux(nodo.siguiente)

    def longitud(self):
        
        contador = 0
        nodo_actual = self.frente

        while nodo_actual is not None:
            contador += 1
            nodo_actual = nodo_actual.siguiente

class Mascota:
    def __init__(self, nombre, especie, edad):
        
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def getName(self):

        return self.nombre

# Creamos algunas mascotas
mascota1 = Mascota("Luna", "Perro", 3)
mascota2 = Mascota("Simba", "Gato", 5)
mascota3 = Mascota("Bolt", "Perro", 2)

listaMascotas  = [mascota1,mascota2,mascota3]
# Creamos una cola y agregamos las mascotas a la cola
cola_mascotas = Cola()
#cola_mascotas.agregar(mascota1)
#cola_mascotas.agregar(mascota2)
#cola_mascotas.agregar(mascota3)

for mascota in listaMascotas:

    cola_mascotas.agregar(mascota)

# Imprimimos todas las mascotas en la cola
cola_mascotas.recorrer()
print("LA LONGITUD ES " , cola_mascotas.longitud())
cola_mascotas.eliminar()
print("RECORRE LA COLA DESPUES DE ELIMINAR LOS ARCHIVOS")
cola_mascotas.recorrer()