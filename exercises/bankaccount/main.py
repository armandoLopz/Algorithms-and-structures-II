class BankAccount:

    def __init__(self, year, month, day, numberAccount, amount, holder):
        
        self.year = year
        self.month = month
        self.day = day
        self.numberAccount = numberAccount
        self.amount = amount
        self.holder = holder

    def statusAccount(self):

        print(f"El estado de la cuenta es de {self.amount}")
    
    def depositMoney(self,name,lastname,id,depositAmount):

        if depositAmount > 0:
            self.amount+= depositAmount
            print(f"Se han depositado la cantidad de {depositAmount} con exito")
        else:
            print("Debe ingresar una cantidad mayor a 0 para poder depositar dinero en la cuenta")

    def retireMoney(self, retireAmount):

        if retireAmount <= self.amount and retireAmount > 0:
            print(f"Se ha retirado la cantida de {retireAmount} con exito")
        elif retireAmount > self.amount and retireAmount > 0:
            print(f"El monto ingresado para retirar es mayor al disponible \nSu saldo disponible es de {self.amount}")
        else:
            print("Debe ingresar unos datos correctos")
        

class Holder:
    
    def __init__(self, id, name, lastName, direction):

        self.id = id
        self.name = name
        self.lastName = lastName
        self.direction = direction

userAccount = Holder(29911900,"Armando", "Lopez", "Naguanagua")
bankAcoounnt = BankAccount(2020, 11,20,"222002020020", 100, userAccount)

bankAcoounnt.depositMoney("Armando", "Lopez","29911900", 0.1)
bankAcoounnt.retireMoney(100)



