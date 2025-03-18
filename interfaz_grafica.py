import tkinter as tk
from tkinter import messagebox
import random

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

class PiedraPapelTijeraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Piedra, Papel o Tijera")

        self.opciones = ["piedra", "papel", "tijera"]

        self.label = tk.Label(root, text="Elige una opción:")
        self.label.pack()

        self.boton_piedra = tk.Button(root, text="Piedra", command=lambda: self.jugar("piedra"))
        self.boton_piedra.pack()

        self.boton_papel = tk.Button(root, text="Papel", command=lambda: self.jugar("papel"))
        self.boton_papel.pack()

        self.boton_tijera = tk.Button(root, text="Tijera", command=lambda: self.jugar("tijera"))
        self.boton_tijera.pack()

    def jugar(self, usuario):
        computadora = random.choice(self.opciones)
        resultado = self.determinar_ganador(usuario, computadora)
        messagebox.showinfo("Resultado", f"Computadora eligió: {computadora}\n{resultado}")

    def determinar_ganador(self, usuario, computadora):
        if usuario == computadora:
            return "¡Empate!"
        elif (usuario == "piedra" and computadora == "tijera") or \
             (usuario == "papel" and computadora == "piedra") or \
             (usuario == "tijera" and computadora == "papel"):
            return "¡Ganaste!"
        else:
            return "¡Perdiste!"

if __name__ == "__main__":
    modo = input("Elige el modo de juego (consola/tkinter): ").strip().lower()
    
    if modo == "consola":
        jugar_multi_jugador()
    elif modo == "tkinter":
        root = tk.Tk()
        app = PiedraPapelTijeraApp(root)
        root.mainloop()
    else:
        print("Modo no válido. Elige 'consola' o 'tkinter'.")

