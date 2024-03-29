class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Cola:

    def __init__(self):
        self.frente = None
        self.fin = None

    def estaVacia(self):
        return self.frente is None
    
    def agregar(self, valor):
        nodo_nuevo = Nodo(valor)

        if self.estaVacia():
            self.frente = nodo_nuevo
        else:
            self.fin.siguiente = nodo_nuevo
        self.fin = nodo_nuevo
            
    def eliminar(self):
        if self.estaVacia():
            return None
        else:
            valor_eliminado = self.frente.valor
            self.frente = self.frente.siguiente
            
            if self.frente is None:
                self.fin = None
            return valor_eliminado
        
    def longitud(self):
        
        contador = 0
        nodo_actual = self.frente

        while nodo_actual is not None:
            contador += 1
            nodo_actual = nodo_actual.siguiente

        return contador

    def vaciar(self):
        self.frente = None
        self.fin = None
    
    def obtener_objetos(self):
        objetos = []
        nodo_actual = self.frente
        while nodo_actual is not None:
            objetos.append(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente
        return objetos
        
    def ver_frente(self):
        
        if self.estaVacia():
            return None
        else:
            return self.frente.valor
        
    def recorrer(self):
        if self.estaVacia():
            return ""
        else:
            return self._recorrer_aux(self.frente)

    def _recorrer_aux(self, nodo):
        
        file = ""

        if nodo is not None:
            
            print(nodo.valor.showDetailsFile())
            return self._recorrer_aux(nodo.siguiente)
        
        return file 