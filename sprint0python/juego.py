import random

moves = {
    1: "piedra",
    2: "papel",
    3: "tijera" 
}

rounds = 1
wins= 0
loses= 0 
game= 0
finish = True

while (rounds<=5):
    UserMove = (input (" Que deseas sacar (piedra/papel/tijera) ?"))
    while (UserMove != "piedra") and (UserMove != "papel") and (UserMove!= "tijera"):
        UserMove = input ("Introduzca uno de los movimientos permitidos")

    MovePC= moves [random.randint(1,3)]

    if UserMove == moves[1] and MovePC == moves[1] or UserMove == moves[2] and MovePC== moves[2] or UserMove == moves[3] and UserMove == MovePC[3]:
        print("Has empatado la ronda, la/el" + UserMove + " empata a la/el " + MovePC)

    elif UserMove == moves[1] and MovePC== moves[3] or UserMove == moves[2] and MovePC == moves[1] or UserMove == moves[3] and MovePC == moves[2]:
        print("Has ganado la ronda,la/el " + UserMove+ " gana a la/el" + MovePC)
        wins = wins + 1
        rounds = rounds +1
    else:
        print("Has perdido la ronda,la/el" + MovePC + " gana a la/el " + UserMove)
        loses = loses + 1
        rounds = rounds +1

if wins > loses:
    print("Has ganado la partida. Felicidades !!!!")
else:
    print("Has perdido la parrida. Inténtalo otra vez")
        



    

