
opcion = " "
contAciertos = 0
opcionMayus=" "

adivinanzas = {
    1 : "El roer es mi trabajo,el queso mi aperitivo y el gato ha sido siempre mi más temido enemigo.", 
    2 : "Me pisas y no me quejo, me cepillas si me mancho, y con mi hermano gemelo, bajo tu cama descanso.",
    3 : "Oro parece, plata no es. Abran las cortinas y verán lo que es.",
}

respuestas = {
    1: "A) Ratón, B) Rata, C) Perro",
    2: "A) Calcetín, B) Zapato, C) Camiseta",
    3: "A) Naranja, B) Platano, C) Fresa"
}

correctas = {
   1:"A",
   2:"B",
   3:"B"
}

print(adivinanzas[1])
print(respuestas[1])
opcion = input ("\n\tTeclea opción? ")
opcionMayus = opcion.upper()

if (opcionMayus==correctas[1]):
    print ("\nFELICIDADES. RESPUESTA CORRECTA !!!!")
    contAciertos = contAciertos +10;

if (opcionMayus!=correctas[1]):
    print(" La opción es incorrecta, has fallado. ")
    contAciertos = contAciertos -5;

opcion = " "

print(adivinanzas[2])
print(respuestas[2])
opcion = input ("\n\tTeclea opción? ")
opcionMayus = opcion.upper();

print(adivinanzas[2])
print(respuestas[2])

if (opcionMayus==correctas[2]):
    print ("\nFELICIDADES. RESPUESTA CORRECTA !!!!")
    contAciertos = contAciertos +10;

if (opcionMayus!=correctas[2]):
    print(" La opción es incorrecta, has fallado. ")
    contAciertos = contAciertos -5;

opcion = " "
opcionMayus= " "

print(adivinanzas[3])
print(respuestas[3])

opcion = input ("\n\tTeclea opción? ")
opcionMayus = opcion.upper();

print(adivinanzas[3])
print(respuestas[3])

if (opcionMayus==correctas[3]):
    print ("\nFELICIDADES. RESPUESTA CORRECTA !!!!")
    contAciertos = contAciertos +10;

if (opcionMayus!=correctas[3]):
    print(" La opción es incorrecta, has fallado. ")
    contAciertos = contAciertos -5;

print ("TU PUNTUACIÓN HA SIDO: ")
print (contAciertos)








