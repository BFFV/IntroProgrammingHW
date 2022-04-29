import tkinter as tk
import random

monto_inicial = 1000
color = "green"

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

        jugador_1 = Jugador(monto_inicial)
        jugador_2 = Jugador(monto_inicial)
        self.jugadores = [jugador_1, jugador_2]

        self.label_monto1 = tk.Label(self, text= "Monto Jugador 1: " + str(monto_inicial))
        self.label_monto2 = tk.Label(self, text= "Monto Jugador 2: " + str(monto_inicial))
        self.labels_montos = [self.label_monto1, self.label_monto2]

        self.crear_carton(1)
        self.crear_carton(2)

        self.contador = set()
        self.apuesta = 0

    def crear_carton(self, jugador):
        self.labels_montos[jugador-1].pack(pady=10)
        word = "BINGO"
        carton = self.jugadores[jugador-1]
        group_master = tk.LabelFrame(self, text="Jugador" + str(jugador), padx=10, pady=10)
        for i in range(5):
            group = tk.LabelFrame(group_master, text=word[i])
            for j in range(5):
                label = tk.Label(group, text=0)
                carton.carton[i].append(label)
                label.grid(row=j,column=i)

            group.pack(padx=10, pady=10, side="left")
        group_master.pack( pady=20)


    # jugador sera 1 o 2
    def colocar_numero(self, pos_y, letra, numero, jugador):
        carton = self.jugadores[jugador-1]
        try:
            label = carton.carton[letra][pos_y]
            label.config(text = numero)
        except KeyError:
            self.master.destroy()
            print("Coordenadas fuera de rango")
            raise KeyError

    def esta_marcado(self, pos_y, letra, jugador):
        carton = self.jugadores[jugador - 1]
        try:
            label = carton.carton[letra][pos_y]
        except:
            self.master.destroy()
            print("Coordenadas fuera de rango")
            raise KeyError

        if label.cget('bg') == "green":
            return True
        else:
            return False


    def mostrar_dinero(self, jugador, monto):
        if jugador == 1:
            self.label_monto1.config(text="Monto Jugador 1: " + str(monto))
            self.jugadores[jugador - 1].monto = monto
        elif jugador == 2:
            self.label_monto2.config(text="Monto Jugador 2: " + str(monto))
            self.jugadores[jugador - 1].monto = monto
        else:
            self.master.destroy()
            print("jugador ingresado incorrecto")
            raise Exception

    def preguntar_monto(self, jugador):
        return self.jugadores[jugador - 1].monto

    def marcar_numero(self, pos_y, letra, marcado,jugador):
        carton = self.jugadores[jugador - 1]
        try:
            label = carton.carton[letra][pos_y]
        except:
            self.master.destroy()
            print("Coordenadas fuera de rango")
            raise KeyError

        if marcado:
            label.config(bg = color)
        else:
            label.config(bg = "White")

    def obtener_numero(self, pos_y, letra, jugador):
        carton = self.jugadores[jugador - 1]
        try:
            label = carton.carton[letra][pos_y]
        except:
            self.master.destroy()
            print("Coordenadas fuera de rango")
            raise KeyError

        return int(label.cget("text"))

    def mostrar_mensaje(self, mensaje):
        self.bolita.config(text=mensaje, font="Helvetica")


    def create_widgets(self):
        self.button = tk.Button(self, text="Siguiente turno")
        self.button.pack(side="bottom")
        self.bolita = tk.Label(self, bd=20)
        self.bolita.pack(side="bottom")

    def reiniciar_contador(self):
        self.contador = set()

    def agregar(self, numero):

        if numero not in self.contador:
            self.contador.add(numero)
            return True
        else:
            return False

    def mostrar_ventana(self, estado):
        if estado:
            self.master.update()
            self.master.deiconify()
        else:
            self.master.withdraw()

    def cerrar_ventana(self):
        self.master.withdraw()
        self.master.destroy()

    def poner_apuesta(self, apuesta):
        self.apuesta = apuesta

    def obtener_apuesta(self):
        return self.apuesta


class Jugador:

    def __init__(self, monto):
        self.carton = {0: [], 1: [], 2: [], 3: [], 4: []}
        self.monto = monto
