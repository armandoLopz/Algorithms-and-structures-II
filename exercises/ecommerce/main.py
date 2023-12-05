class Product:

    def __init__(self,id, name, description, count, amount):
        
        self.id = id
        self.name = name
        self.description = description
        self.count = count
        self.amount = amount

    def datailsProduct(self):

        print(f"Detalles del producto:\nId: {self.id}\nName: {self.name}\nDescripcion: {self.description}\nCantidad: {self.count}\nMonto: {self.amount}")

class User:
    
    def __init__(self, id, name, lastname, email, direction):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.email = email
        self.direction = direction

class ShoppingCart:

    def __init__(self, products = [], user = "none"):

        self.products = products
        self.user = user

    def aggProduct(self, product):
        if product.count > 0 and product.amount > 0 :
            self.products.append(product)
            print("Se ha agregado el producto correctamente")
        else:
            print("Debe introducir unos datos correctos")
            
    def showProducts(self):
        if len(self.products) > 0:
            for product in self.products:
                product.datailsProduct()
        else:
            print("No hay productos en el carrito")

userShop = User(1, "Armando", "Lopez", "arm@gmail.com", "Naguanagua")
cart = ShoppingCart([], userShop)

product1y = Product(1, "T shirts", "White t shirts, 100% linen",2,10)
cart.aggProduct(product1y)

producty = Product(2, "Jeans", "Cordoury denim jeans", 3, 40)
cart.aggProduct(product1y)

cart.showProducts()