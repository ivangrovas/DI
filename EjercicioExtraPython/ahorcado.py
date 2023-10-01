from random import choice

choose=True

while choose==True:
    
    print (' [?] Elija dificultad:')
    print ()
    print ('1- Fácil')
    print ('2- Normal')
    print ('3- Difícil')

    option = int(input())

    #Emulamos un switch definiendo una función

    def switch (option):

        if option==1:
            return ('Facil')
        elif option==2:
            return ('Normal')
        return ('Dificil')
    
    i=switch(option) #Guardamos el valor de la opción option en la variable i

    #Abrimos de lectura el fichero donde tenemos las palabras guardadas

    with open ("palabras.txt","r") as reading:

        reader=reading.read().splitlines() #Dividimos el texto del txt en subcadenas con splitlines
        reader=choice(reader [reader.index(i):(reader.index(i)+3)]) #Escogemos aleatoriamente una palabra con choice y buscamos con index las palabras correspondientes al nivel de dificultad elegido 
        
    re_writable=''
    total_letters=''

    for i in range(len(reader)):
        re_writable=re_writable + '_'
    
    print(re_writable) #Mostramos la palabra elegida con los guiones bajos, es decir, oculta.regrabableop

    opportunities=0 

    while re_writable!=reader and opportunities<6:

        building_word='' #Un string vacío para ir constuyendo la palabra durante el ahorcado
        letter=input('Escribe una letra que pienses que puede estar en la palabra\n')

        for i in range(len(reader)):

            if letter==reader[i]: #Bucle por si acierta la letra , guardarla en la palabra que estamos construyendo 
                building_word+=letter 
                choose=False
            else:
                building_word+=re_writable[i] #Bucle por si falla la letra , guardar un guión bajo en la posición de la letra que estamos construyendo 
                choose=True

        re_writable=building_word 
        total_letters = total_letters + letter #Registro de las letras usadas inválidas

        opportunities+=1

        print (re_writable)
        print ('LLevas '+str(opportunities)+ ', oportunidades gastadas (Máximo 6)')
        print ('Letras probadas: '+total_letters)

    if opportunities>=6: 
       print ('La palabra era: '+reader + ', has perdido')
    else:
        print (' [!] FELICIDADES, HAS RESUELTO EL AHORCADO')

    if input('¿Quieres jugar otra partida? (s/n)')=='s':
        choose=True
    else:
        choose=False