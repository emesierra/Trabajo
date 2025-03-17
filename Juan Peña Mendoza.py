def jugar_multi_jugador():
    jugador1 = input("Jugador 1, elige piedra, papel o tijera: ").lower()
    jugador2 = input("Jugador 2, elige piedra, papel o tijera: ").lower()

    opciones = ["piedra", "papel", "tijera"]

    if jugador1 not in opciones or jugador2 not in opciones:
        print("Opción no válida. Intenta de nuevo.")
        return

    if jugador1 == jugador2:
        print("¡Empate!")
    elif (jugador1 == "piedra" and jugador2 == "tijera") or \
         (jugador1 == "papel" and jugador2 == "piedra") or \
         (jugador1 == "tijera" and jugador2 == "papel"):
        print("¡Jugador 1 gana!")
    else:
        print("¡Jugador 2 gana!")

if _name_ == "_main_":
    jugar_multi_jugador()
