def jugar_con_mejoras():
    victorias = 0
    derrotas = 0

    while True:
        opciones = ["piedra", "papel", "tijera"]
        computadora = random.choice(opciones)
        usuario = input("Elige piedra, papel o tijera (o 'salir' para terminar): ").lower()

        if usuario == "salir":
            break

        if usuario not in opciones:
            print("Opción no válida. Intenta de nuevo.")
            continue

        print(f"Computadora eligió: {computadora}")

        if usuario == computadora:
            print("¡Empate!")
        elif (usuario == "piedra" and computadora == "tijera") or \
             (usuario == "papel" and computadora == "piedra") or \
             (usuario == "tijera" and computadora == "papel"):
            print("¡Ganaste!")
            victorias += 1
        else:
            print("¡Perdiste!")
            derrotas += 1

        print(f"Victorias: {victorias}, Derrotas: {derrotas}")

if __name__ == "__main__":
    jugar_con_mejoras()