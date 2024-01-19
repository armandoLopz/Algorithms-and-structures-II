class factura:

    def __init__(self, id, descripcion,  cantidad, precio):

        self.id = id
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio = precio

    def getId(self, id):

        self.id = id

        return self.id
    
    def getDescription(self, descripcion):

        self.descripcion = descripcion
        
        return self.descripcion
    
    def getCantidad(self, cantidad):

        self.cantidad = cantidad
        
        return self.cantidad
    
    def getPrice(self, precio):

        self.precio = precio
        
        return self.precio
    
    def showId(self):

        return self.id
    
    def showDescription(self):

        return self.descripcion
    
    def showCantidad(self):

        return self.cantidad
    
    def showPrice(self):

        return self.precio
    
    def getAmount(self):

        if self.cantidad > 0 and self.precio > 0:

            amount = self.cantidad*self.precio
            return amount
        
        elif self.cantidad < 0 and self.precio > 0:
            
            return "La cantidad ingresa es invalida"
        
        elif self.cantidad > 0 and self.precio <= 0:

            return "El precio introducido es invalido"
        
factur = factura("11" ,"aa",25,10.25)
print(factur.showId())


print(factur.getId("44"))
print(factur.showId())