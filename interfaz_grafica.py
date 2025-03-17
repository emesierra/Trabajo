import tkinter as tk
from tkinter import messagebox
import random

class PiedraPapelTijeraApp:
    def __init__(self, root):  # ← CORREGIDO
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

# ← CORREGIDO
if __name__ == "__main__":
    root = tk.Tk()
    app = PiedraPapelTijeraApp(root)
    root.mainloop()
