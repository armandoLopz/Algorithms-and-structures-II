class NodoNArio:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

class ArbolNArio:
    def __init__(self):
        self.raiz = None
    
    def getRaiz(self):

        return self.raiz.valor
    def esta_vacio(self):
        return self.raiz is None
        
    def insertar(self, valor, padre=None):
        nuevo_nodo = NodoNArio(valor)

        if padre is None:
            if self.raiz is None:
                self.raiz = nuevo_nodo
            else:
                raise ValueError("El árbol ya tiene una raíz")
        else:
            padre_nodo = self._buscar_nodo(padre, self.raiz)
            if padre_nodo is not None:
                padre_nodo.hijos.append(nuevo_nodo)
            else:
                raise ValueError("No se encontró el nodo padre")

    def _buscar_nodo(self, valor, nodo_actual):
        if nodo_actual.valor == valor:
            return nodo_actual
        for hijo in nodo_actual.hijos:
            resultado = self._buscar_nodo(valor, hijo)
            if resultado is not None:
                return resultado
        return None

    def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(valor, self.raiz)

    def _eliminar_recursivo(self, valor, nodo_actual):
        if nodo_actual.valor == valor:
            return None
        nuevos_hijos = []
        for hijo in nodo_actual.hijos:
            nuevo_hijo = self._eliminar_recursivo(valor, hijo)
            if nuevo_hijo is not None:
                nuevos_hijos.append(nuevo_hijo)
        nodo_actual.hijos = nuevos_hijos
        return nodo_actual

    def modificar(self, valor_viejo, valor_nuevo):
        self.eliminar(valor_viejo)
        self.insertar(valor_nuevo)

    def consultar(self, valor):
        return self._consultar_recursivo(valor, self.raiz)

    def _consultar_recursivo(self, valor, nodo_actual):
        if nodo_actual.valor == valor:
            return nodo_actual
        for hijo in nodo_actual.hijos:
            resultado = self._consultar_recursivo(valor, hijo)
            if resultado is not None:
                return resultado
        return None

    def preorden(self):
   
        self._preorden_recursivo(self.raiz)

    def _preorden_recursivo(self, nodo_actual):
        if nodo_actual is not None:
     
            for hijo in nodo_actual.hijos:    
                print(hijo.valor.getNamefile())

    def postorden(self):
        self._postorden_recursivo(self.raiz)

    def _postorden_recursivo(self, nodo_actual):
        if nodo_actual is not None:
            for hijo in nodo_actual.hijos:
                self._postorden_recursivo(hijo)
            print(nodo_actual.valor, end=" ")

    def inorden(self):
        self._inorden_recursivo(self.raiz)

    def _inorden_recursivo(self, nodo_actual):
        if nodo_actual is not None:
            for hijo in nodo_actual.hijos:
                self._inorden_recursivo(hijo)
            print(nodo_actual.valor, end=" ")

""""
# Crear el árbol y realizar las operaciones
arbol = ArbolNArio()
arbol.insertar(1)
arbol.insertar(2, 1)
arbol.insertar(3, 1)
arbol.insertar(4, 2)
arbol.insertar(5, 2)
arbol.insertar(6, 3)

print(arbol.getRaiz())
print("Recorrido en Preorden:")
arbol.preorden()

print("\nRecorrido en Inorden:")
arbol.inorden()

print("\nRecorrido en Postorden:")
arbol.postorden()"""