def factorial(number):

    if number == 0:
        return 1
    else:
        return number * factorial(number-1)

valueNumber = int(input("Ingrese un numero: "))

factor = factorial(valueNumber)

print(f"El factorial de {valueNumber} es igual a {factor}")