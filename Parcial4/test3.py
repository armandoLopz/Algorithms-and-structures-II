class MiClase:
    def __init__(self):
        self.valor = 0

    def mi_metodo(self):
        print("Este es el método mi_metodo.")

    def otro_metodo(self):
        print("Este es otro método.")
        self.mi_metodo()  # Llamada al método mi_metodo dentro de otro_metodo

# Crear una instancia de la clase
objeto = MiClase()

# Llamar al método otro_metodo
objeto.otro_metodo()