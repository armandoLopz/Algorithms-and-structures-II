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
            print(nodo.valor)
            self._recorrer_aux(nodo.siguiente)
