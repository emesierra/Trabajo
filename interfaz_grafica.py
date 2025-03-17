import tkinter as tk
from tkinter import messagebox
import random

class PiedraPapelTijeraApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Piedra, Papel o Tijera")

        self.opciones = ["piedra", "papel", "tijera"]
        self.victorias = 0
        self.derrotas = 0

        # Interfaz gráfica
        self.label = tk.Label(root, text="Elige una opción:")
        self.label.pack()

        self.boton_piedra = tk.Button(root, text="Piedra", command=lambda: self.jugar("piedra"))
        self.boton_piedra.pack()

        self.boton_papel = tk.Button(root, text="Papel", command=lambda: self.jugar("papel"))
        self.boton_papel.pack()

        self.boton_tijera = tk.Button(root, text="Tijera", command=lambda: self.jugar("tijera"))
        self.boton_tijera.pack()

        # Botón para modo multi-jugador
        self.boton_multi = tk.Button(root, text="Modo Multi-Jugador", command=self.jugar_multi_jugador)
        self.boton_multi.pack()

        # Contador de victorias y derrotas
        self.label_resultado = tk.Label(root, text=f"Victorias: {self.victorias}, Derrotas: {self.derrotas}")
        self.label_resultado.pack()

    def jugar(self, usuario):
        # Lógica del juego contra la computadora
        computadora = random.choice(self.opciones)
        resultado = self.determinar_ganador(usuario, computadora)
        self.actualizar_marcador(resultado)
        messagebox.showinfo("Resultado", f"Computadora eligió: {computadora}\n{resultado}")

    def jugar_multi_jugador(self):
        # Ventana para el modo multi-jugador
        ventana_multi = tk.Toplevel(self.root)
        ventana_multi.title("Modo Multi-Jugador")

        label_jugador1 = tk.Label(ventana_multi, text="Jugador 1, elige piedra, papel o tijera:")
        label_jugador1.pack()

        entrada_jugador1 = tk.Entry(ventana_multi)
        entrada_jugador1.pack()

        label_jugador2 = tk.Label(ventana_multi, text="Jugador 2, elige piedra, papel o tijera:")
        label_jugador2.pack()

        entrada_jugador2 = tk.Entry(ventana_multi)
        entrada_jugador2.pack()

        def determinar_ganador_multi():
            # Lógica del modo multi-jugador
            jugador1 = entrada_jugador1.get().lower()
            jugador2 = entrada_jugador2.get().lower()

            if jugador1 not in self.opciones or jugador2 not in self.opciones:
                messagebox.showerror("Error", "Opción no válida. Intenta de nuevo.")
                return

            if jugador1 == jugador2:
                resultado = "¡Empate!"
            elif (jugador1 == "piedra" and jugador2 == "tijera") or \
                 (jugador1 == "papel" and jugador2 == "piedra") or \
                 (jugador1 == "tijera" and jugador2 == "papel"):
                resultado = "¡Jugador 1 gana!"
            else:
                resultado = "¡Jugador 2 gana!"

            messagebox.showinfo("Resultado", resultado)

        boton_jugar = tk.Button(ventana_multi, text="Jugar", command=determinar_ganador_multi)
        boton_jugar.pack()

    def determinar_ganador(self, usuario, computadora):
        # Lógica para determinar el ganador
        if usuario == computadora:
            return "¡Empate!"
        elif (usuario == "piedra" and computadora == "tijera") or \
             (usuario == "papel" and computadora == "piedra") or \
             (usuario == "tijera" and computadora == "papel"):
            return "¡Ganaste!"
        else:
            return "¡Perdiste!"

    def actualizar_marcador(self, resultado):
        # Actualiza el contador de victorias y derrotas
        if "Ganaste" in resultado:
            self.victorias += 1
        elif "Perdiste" in resultado:
            self.derrotas += 1
        self.label_resultado.config(text=f"Victorias: {self.victorias}, Derrotas: {self.derrotas}")

if _name_ == "_main_":
    root = tk.Tk()
    app = PiedraPapelTijeraApp(root)
    root.mainloop()