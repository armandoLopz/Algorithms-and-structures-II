import sys

sys.setrecursionlimit(5000)

#def sumList(number = []):

listNumbers = [] 

def createlist():

    def decitionNumbers():

        decision = int(input("1- Para ingresar los numeros de una lista\n0- Para salir del programa: "))

        return decision

    number = decitionNumbers()

    while number != 0: 

        number = int(input("Inserte un numero para agregarlo a la lista"))
        listNumbers.append(number)

        decitionNumbers()

def factorial(number):

    if number <= 1:

        return 1
    
    else:
        return number*factorial(number-1)


#number = int(input("Ingrese un numero"))

#print(factorial(number))

def palindrome(palabra):

    if len(palabra) <= 1:
        return True
    elif palabra[0] == palabra[-1]:
        return palindrome(palabra[1:-1])
    else:
        return False
    

#print(palindrome("juan"))

def countDigits(number):

    countDigits = 0

    if  number < 10:

        return 1 
    
    else:
        return 1+ countDigits(number // 10)
    

def countNumbers(count,number2):


    if number2 == 0:
        
        return 1
    
    else:
        count+=1
        
        return count,countNumbers(count,number2-1)

print(countNumbers(0,3))

    
    

