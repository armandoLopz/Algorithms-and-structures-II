class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Pila:
    
    def __init__(self):
        
        self.tope = None

    def estaVacia(self):
        
        return self.tope is None
    
    def agregar(self, valor):
        
        nodo_nuevo = Nodo(valor)
        nodo_nuevo.siguiente = self.tope
        self.tope = nodo_nuevo
    
    def vaciar_pila(self):
        while not self.estaVacia():
            self.eliminar()
    
    def eliminar(self):
        
        if self.estaVacia():
            return None
        else:
            valor_eliminado = self.tope.valor
            self.tope = self.tope.siguiente
            return valor_eliminado
    
    def obtener_objetos(self):
        objetos = []
        nodo_actual = self.tope
        while nodo_actual is not None:
            objetos.append(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente
        return objetos
        
    def ver_tope(self):
        
        if self.esta_vacia():
            return None
        else:
            return self.tope.valor
        
    def recorrer(self):

        if self.estaVacia():
            print("La pila está vacía")
        else:
            return self._recorrer_aux(self.tope)

    def _recorrer_aux(self, nodo):

        file = ""

        if nodo is not None:
            print("                 Subcarpeta: " + nodo.valor.getNameFolder())
            print(nodo.valor.contentFolder())
            self._recorrer_aux(nodo.siguiente)
        
        return file