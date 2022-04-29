from Tarea_1 import *

root = tk.Tk()
root.geometry('{}x{}'.format("550", "650"))
app = Application(master=root)

def turno():
    # AQUI DENTRO EMPIEZA CADA TURNO
    pass # eliminar esta linea una vez hayan escrito algo aqui

# Aqui empieza su programa


# ESTO NO SE TOCA
app.button.config(command=turno)
app.mainloop()
