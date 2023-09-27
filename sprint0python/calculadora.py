from operaciones import suma, resta, multiplicacion, division
## import operaciones

repetir = True
otra = " "
opcion = " "

operaciones = {
    1: "suma",
    2: "resta",
    3: "multiplicacion",
    4: "division"
}

while (repetir == True) :

    opcion = (input (" Que operación desea realizar (suma/resta/multiplicacion/division) ?"))
    while (opcion != "suma") & (opcion != "resta") & (opcion != "multiplicacion") & (opcion != "division"):
        opcion = input ("Introduzca el nombre de una de las 4 operaciones disponibles")
        
    num1= float(input ("Introduzca el primer número con el que desea operar ?"))
    num2= float(input ("Introduzca el segundo número con el que desea operar ?"))

    if opcion==operaciones[1]:
        print(suma(num1,num2))

    if opcion==operaciones[2]:
        print(resta(num1,num2))

    if opcion==operaciones[3]:
        print(multiplicacion(num1,num2))

    if opcion==operaciones[4]:
        print(division(num1,num2))

    otra = input ("Desea realizar otra operación (y/n) ? ")

    num1=0 
    num2=0
    
    if (otra=="n"):
        repetir=False
        
    



