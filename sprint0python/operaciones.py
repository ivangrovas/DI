num1 = 0
num2 = 0

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    if (num2 == 0): 
        print ("ERROR: No se puede dividir entre 0")
    else:
        return num1 / num2