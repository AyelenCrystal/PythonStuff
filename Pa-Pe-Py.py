def inicio_juego():
    "Muestra la ficha elegida por cada usuario"
    print("Pa - Pe - Py" )
    print()
    print("Elige tu ficha:")
    print()
    print(" O / X")

    ficha = " "
    while ficha != "O" and ficha != "X":
        ficha = input(" ").upper()

    if ficha == "O":
        Jugador_1_ficha = "O"
        Jugador_2_ficha = "X"
    else:
        Jugador_1_ficha = "X"
        Jugador_2_ficha = "O"

    return Jugador_1_ficha, Jugador_2_ficha

def tablero_inicial(tablero):
    "Muestra el tablero con las casillas vacias para iniciar el juego"
    tablero2 = [
        [tablero[0], '|', tablero[1], '|', tablero[2]],
        ["--+---+--"],
        [tablero[3], '|', tablero[4], '|', tablero[5]],
        ["--+---+--"],
        [tablero[6], '|', tablero[7], '|', tablero[8]],
    ]

    for nFila in tablero2:
        for i in range(len(nFila)):
            if i == len(nFila) - 1:
                print(nFila[i], end= '\n')
            else:
                print(nFila[i], end= ' ')


def durante_juego(tablero):
    "Comprueba si el tablero esta lleno o vacio"
    for i in tablero:
        if i == " ":
            return False
    else:
        return True

def casilla(tablero, jugada, turno1):
    "Devuelve True si una casilla esta libre o False si esta llena"
    if tablero[jugada] == " ":
        if turno1:
            tablero[jugada] = Jugador_1_ficha
        else:
            tablero[jugada] = Jugador_2_ficha
        return True

def ganador(tablero, jugador):
    "Verifica si hay un ganador"
    if tablero[0] == tablero[1] == tablero[2] == jugador or \
       tablero[3] == tablero[4] == tablero[5] == jugador or \
       tablero[6] == tablero[7] == tablero[8] == jugador or \
       tablero[0] == tablero[4] == tablero[8] == jugador or \
       tablero[2] == tablero[4] == tablero[6] == jugador or \
       tablero[0] == tablero[3] == tablero[6] == jugador or \
       tablero[1] == tablero[4] == tablero[7] == jugador or \
       tablero[2] == tablero[5] == tablero[8] == jugador:
        return True
    else:
        return False


inicio_juego()

tablero = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
      
turno_1 = True
Jugador_1 = ""
Jugador_2 = ""
Jugador_1_ficha = "X"
Jugador_2_ficha = "O"
turno = 0

tablero_inicial(tablero)

while turno < 9:
    if Jugador_1 == " ":
        print("Nombre de Jugador 1: ")
        Jugador_1 = input()
        print("Nombre de Jugador 2: ")
        Jugador_2 = input()
    else:
        if turno_1:
            print(Jugador_1 + ', elige una posicion')
        else:
            print(Jugador_2 + ', elige una posicion')

        jugada = int(input())

        valor = casilla(tablero, jugada, turno_1)
        if valor == True:
            turno_1 = not turno_1
            turno += 1
            tablero_inicial(tablero)
            if ganador(tablero, Jugador_1_ficha) == True:
                print(Jugador_1 + " gano!")
                break
            elif ganador(tablero, Jugador_2_ficha) == True:
                print(Jugador_2 + " gano!")
                break
        else:
            print(valor)
        
        if turno == 9:
            print("Empate...")



