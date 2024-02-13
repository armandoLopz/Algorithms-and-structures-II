class Nodo:
    def __init__(self, valor=None):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:

    def __init__(self):
        self.cabeza = None
        self.longitud = 0

    def __len__(self):
        return self.longitud

    def __iter__(self):
        actual = self.cabeza
        while actual:
            yield actual.valor
            actual = actual.siguiente
            
    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo

        else:
            actual = self.cabeza

            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

        self.longitud += 1

    def eliminar(self, valor):

        if self.cabeza is None:
            return False
        
        if self.cabeza.valor == valor:
            
            self.cabeza = self.cabeza.siguiente
            self.longitud -= 1

            return True
        actual = self.cabeza

        while actual.siguiente:
            
            if actual.siguiente.valor == valor:
                actual.siguiente = actual.siguiente.siguiente
                self.longitud -= 1
                return True
            actual = actual.siguiente
        return False
    
    def insertar(self, indice, valor):
        
        if indice < 0 or indice > self.longitud:
            raise IndexError("Índice fuera de rango")
        
        nuevo_nodo = Nodo(valor)
        if indice == 0:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            for i in range(indice - 1):
                actual = actual.siguiente

            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo

        self.longitud += 1

    def obtener(self, indice):
        if indice < 0 or indice >= self.longitud:
            raise IndexError("Índice fuera de rango")
        actual = self.cabeza
        for i in range(indice):
            actual = actual.siguiente
        return actual.valor
    
    def index(self, valor):
        
        actual = self.cabeza
        indice = 0
        while actual:
            if actual.valor == valor:
                return indice
            actual = actual.siguiente
            indice += 1
        raise ValueError("{} no está en la lista".format(valor))

    def pop(self, indice=None):

        if indice is None:
            indice = self.longitud - 1

        if indice < 0 or indice >= self.longitud:
            raise IndexError("Índice fuera de rango")
        
        if indice == 0:
            valor = self.cabeza.valor
            self.cabeza = self.cabeza.siguiente
            self.longitud -= 1

            return valor
        actual = self.cabeza
        
        for i in range(indice - 1):

            actual = actual.siguiente
            valor = actual.siguiente.valor
            actual.siguiente = actual.siguiente.siguiente
            self.longitud -= 1
            return valor
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

        
# Ejemplo de uso:
autos = ListaEnlazada()
autos.agregar(Carro("Toyota", "Corolla"))
# Creamos algunos objetos de la clase Carro
carro1 = Carro("Toyota", "Corolla")
carro2 = Carro("Honda", "Accord")
carro3 = Carro("Ford", "Mustang")
carro4 = Carro("Chevrolet", "Camaro")
# Creamos la lista enlazada y agregamos algunos carros
autos = ListaEnlazada()
autos.agregar(carro1)
autos.agregar(carro2)
autos.agregar(carro3)
# Mostramos los valores de la lista
print(list(autos)) # [carro1, carro2, carro3]
# Insertamos un nuevo carro en el índice 1
autos.insertar(1, carro4)
# Mostramos los valores de la lista
print(list(autos)) # [carro1, carro4, carro2, carro3]
# Eliminamos el carro en el índice 2
autos.eliminar(carro2)
# Mostramos los valores de la lista
print(list(autos)) # [carro1, carro4, carro3]
# Obtenemos el valor del carro en el índice 1
print(autos.obtener(1)) # carro4
# Obtenemos el índice del carro1
print(autos.index(carro1)) # 0
# Eliminamos el último carro de la lista
autos.pop()
# Mostramos los valores de la lista
print(list(autos)) # [carro1, carro4]

print(autos.__iter__())