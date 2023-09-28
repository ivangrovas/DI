
import random


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

keys_adivinanzas = random.sample([1,2,3],2)

for num in keys_adivinanzas:
    print(adivinanzas[num])
    print(respuestas[num])
    opcion = input ("\n\tTeclea opción? ")
    opcionMayus = opcion.upper()
    
    if (opcionMayus==correctas[num]):
        print ("\nFELICIDADES. RESPUESTA CORRECTA !!!!")
        contAciertos = contAciertos +10;

    if (opcionMayus!=correctas[num]):
        print(" La opción es incorrecta, has fallado. ")
        contAciertos = contAciertos -5;

print ("TU PUNTUACIÓN HA SIDO: ")
print (contAciertos)








