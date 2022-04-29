import time
class Simulacion:
    def __init__(self, main, obj, equip, tests):
        self.main = main
        self.obj = obj
        self.equip = equip
        self.tests = tests
    def Mostrar_Equipo(self):
        print("Stats Actuales: V", self.main.life, "D", self.main.dex, "R", self.main.end, "I", self.main.int, "S",
              self.main.luck, "\n")
        l = self.equip
        for i in range(len(l)):
            print(str((i + 1)) + ".- " + l[i].name + ": Bonificador " + str(l[i].bon) + " a " + l[i].stat)
        print("")
    def Mostrar_Items(self):
        print("Stats Actuales: V", self.main.life, "D", self.main.dex, "R", self.main.end, "I", self.main.int, "S", self.main.luck)
        print("Tiempo Disponible:", self.main.time, "\n")
        l = self.obj
        for i in range(len(l)):
            print(str((i + 1)) + ".- " + " (Cantidad: " + str(l[i].stock) + ") " + l[i].name + ": " + str(l[i].cost) + " de tiempo, " + str(l[i].bon) + " de " + l[i].stat)
        print("")
class Personaje:
    def __init__(self, name, life, time, stats):
        self.name = name
        self.life = life
        self.time = time
        self.stats = stats
        self.dex = 0
        self.end = 0
        self.int = 0
        self.luck = 0
        self.datos = [[self.name]]
        self.items = []
        self.equipo = []
    def Equipar(self, obj):
        att = obj.stat
        if att == "vida":
            self.life = int(self.life * obj.bon)
        elif att == "destreza":
            self.dex = int(self.dex * obj.bon)
        elif att == "resistencia":
            self.end = int(self.end * obj.bon)
        elif att == "inteligencia":
            self.int = int(self.int * obj.bon)
        elif att == "suerte":
            self.luck = int(self.luck * obj.bon)
        self.equipo.append(obj.name)
    def Item(self, obj):
        if self.time < obj.cost:
            print("No te queda suficiente tiempo para realizar esta acción!!!" + "\n")
            stock = "Fake"
            return stock
        else:
            self.time -= obj.cost
            att = obj.stat
            if att == "vida":
                self.life += obj.bon
            elif att == "destreza":
                self.dex += obj.bon
            elif att == "resistencia":
                self.end += obj.bon
            elif att == "inteligencia":
                self.int += obj.bon
            elif att == "suerte":
                self.luck += obj.bon
            stock = obj.stock - 1
            self.items.append(obj.name)
            return stock
    def Estado(self):
        restore = [self.life, self.dex, self.end, self.int, self.luck]
        return restore
    def Restaurar(self, estado):
        self.life = estado[0]
        self.dex = estado[1]
        self.end = estado[2]
        self.int = estado[3]
        self.luck = estado[4]
    def Final(self, tests):
        self.datos.append([self.life, self.dex, self.end, self.int, self.luck, self.time])
        loss = self.datos[1][0] - self.life
        self.datos.append([loss])
        self.datos.append([tests[0].name, tests[1].name, tests[2].name])
        self.items.sort()
        while len(self.items) != 0:
            c = 0
            n = self.items[0]
            if "Ã±" in n:
                n = n.replace("Ã±", "ñ")
            for i in range(len(self.items)):
                if self.items[i] != n:
                    break
                else:
                    c += 1
            for i in range(c):
                self.items.pop(0)
            self.datos.append([n, c])
        for i in self.equipo:
            if "Ã±" in i:
                i = i.replace("Ã±", "ñ")
            self.datos.append([i])
        tiempo = self.datos[1][5] - self.time
        self.datos.append([tiempo])
class Prueba:
    def __init__(self, name, life, dex, end, int, luck, weak):
        self.name = name
        self.life = life
        self.dex = dex
        self.end = end
        self.int = int
        self.luck = luck
        self.weak = weak
    def Evaluación(self, main):
        print("Ha llegado la hora de enfrentarse a la evaluación!!!")
        print("Prepárate " + main.name + " para enfrentar a la " + self.name + " (Música Dramática)!!!")
        print("Esta prueba posee V", self.life, "D", self.dex, "R", self.end, "I", self.int, "S",
              self.luck, "y es débil contra la", self.weak, ", ¿Lograrás aprobarla?", "\n")
        print("2 horas después...." + "\n")
        time.sleep(4)
        print("Ha terminado la evaluación!!!, ahora a esperar los resultados (Música Tensa)!!")
        print("2 semanas después...." + "\n")
        time.sleep(4)
        att = self.weak
        if att == "vida":
            w = main.life
        elif att == "destreza":
            w = main.dex
        elif att == "resistencia":
            w = main.end
        elif att == "inteligencia":
            w = main.int
        elif att == "suerte":
            w = main.luck
        dexdif = main.dex - self.dex
        enddif = main.end - self.end
        intdif = main.int - self.int
        luckdif = main.luck - self.luck
        if w == 0:
            w = 1
        daño = (dexdif + enddif + intdif + luckdif) * (self.life // w)
        if (main.life + daño) <= 0:
            print("No pudiste aprobar el semestre!!!, has perdido ):" + "\n")
            time.sleep(2)
            return False
        elif daño >= 0:
            print("Excelente, has aprobado con un puntaje perfecto!!!" + "\n")
            time.sleep(2)
            return True
        else:
            print("Bien hecho!!!, has superado la prueba, pero perdiste", (-1* daño), "puntos de vida" + "\n")
            time.sleep(2)
            return daño
class Consumible:
    def __init__(self, name, stock, stat, bon, cost):
        self.name = name
        self.stock = stock
        self.stat = stat
        self.bon = bon
        self.cost = cost
class Equipamiento:
    def __init__(self, name, stat, bon):
        self.name = name
        self.stat = stat
        self.bon = bon
def Cargar():
    data = []
    file = open("base.txt", 'r', encoding="utf-8")
    for i in file:
        data.append(i.strip())
    file.close()
    return data
# en Cargar se cambia el archivo base
load = Cargar()
config = load
points = config.pop(0).split(",")
num = config.pop(0).split(",")
items = []
for i in range(int(num[0])):
    items.append(config.pop(0).split(","))
equipment = []
for i in range(int(num[1])):
    equipment.append(config.pop(0).split(","))
pruebas = []
for i in range(3):
    pruebas.append(config.pop(0).split(","))
juego = True
print("Bienvenido al Simulador de Interrogaciones!!!")             # Inicio del programa
nombre = False
while nombre == False:
    name = input("Ingresa el nombre de tu personaje:")
    if name == "":
        print("Debes Ingresar un Nombre!!!")
    else:
        nombre = True
main = Personaje(name, int(points[0]), int(points[1]), int(points[2]))
print("Ok " + main.name + ", actualmente posees:")
print(main.life, "puntos de Vida Base")
print(main.time, "puntos de Tiempo")
print(main.stats, "puntos Iniciales para repartir en tus Stats" + "\n")
print("¿Cómo deseas repartir tus", main.stats, "puntos? (Sólo cantidades enteras)")
listo = False
while listo == False:
    main.stats = int(points[2])
    repartir = False
    print("Vida:")
    hp = int(input())
    main.stats -= hp
    if main.stats < 0:
        print("Has excedido la cantidad de puntos que tenías disponible!!!")
        print("Repartiremos de nuevo los puntos desde el inicio")
        repartir = True
    if repartir == False:
        print("Destreza:")
        destreza = int(input())
        main.stats -= destreza
        if main.stats < 0:
            print("Has excedido la cantidad de puntos que tenías disponible!!!")
            print("Repartiremos de nuevo los puntos desde el inicio")
            repartir = True
    if repartir == False:
        print("Resistencia:")
        resistencia = int(input())
        main.stats -= resistencia
        if main.stats < 0:
            print("Has excedido la cantidad de puntos que tenías disponible!!!")
            print("Repartiremos de nuevo los puntos desde el inicio")
            repartir = True
    if repartir == False:
        print("Inteligencia:")
        inteligencia = int(input())
        main.stats -= inteligencia
        if main.stats < 0:
            print("Has excedido la cantidad de puntos que tenías disponible!!!")
            print("Repartiremos de nuevo los puntos desde el inicio")
            repartir = True
    if repartir == False:
        print("Suerte:")
        suerte = int(input())
        main.stats -= suerte
        if main.stats < 0:
            print("Has excedido la cantidad de puntos que tenías disponible!!!")
            print("Repartiremos de nuevo los puntos desde el inicio")
            repartir = True
    if repartir == False:
        listo =True
        main.life += hp
        main.dex = destreza
        main.end = resistencia
        main.int = inteligencia
        main.luck = suerte
        if main.stats > 0:
            print("Te sobraron puntos por usar!!!, estos se agregarán a tu Suerte, ya que la necesitarás!!!")
            main.luck += main.stats
            main.stats = 0
print("Tus Stats iniciales son:")
print("Vida:", main.life, "Destreza:", main.dex, "Resistencia:", main.end, "Inteligencia:", main.int, "Suerte:", main.luck, "\n")
obj = []
for i in items:
    obj.append(Consumible(i[0], int(i[1]), i[2], int(i[3]), int(i[4])))
equip = []
for i in equipment:
    equip.append(Equipamiento(i[0], i[1], float(i[2])))
tests = []
for i in pruebas:
    tests.append(Prueba(i[0], int(i[1]), int(i[2]), int(i[3]), int(i[4]), int(i[5]), i[6]))
sim = Simulacion(main, obj, equip, tests)
sim.main.datos.append([sim.main.life, sim.main.dex, sim.main.end, sim.main.int, sim.main.luck, sim.main.time])
print("A continuación encontrarás el listado de todos los equipamientos disponibles")
print("Ingresa el número asociado para equiparlos (Máximo 3)")
print("Cuando quieras dejar de equipar ingresa -1" + "\n")
equiped = False
ceq = 0
while equiped == False:
    sim.Mostrar_Equipo()
    neq = int(input())
    if neq == -1:
        equiped = True
    elif neq not in range(1, len(sim.equip) + 1):
        print("Debes ingresar un número del 1 al", len(sim.equip), "!!!")
    else:
        sim.main.Equipar(sim.equip[neq - 1])
        sim.equip.pop(neq - 1)
        ceq += 1
        if ceq >= 3:
            print("Se alcanzó el equipamiento máximo(3)!!!" + "\n")
            equiped = True
print("A continuación encontrarás los consumibles disponibles")
print("Ingresa el número asociado para utilizarlos")
print("Cuando quieras comenzar la evaluación ingresa -1" + "\n")
estado = sim.main.Estado()
prep = False
while prep == False:
    sim.Mostrar_Items()
    nit = int(input())
    if nit == -1:
        prep = True
    elif nit not in range(1, len(sim.obj) + 1):
        print("Debes ingresar un número del 1 al", len(sim.obj), "!!!")
    else:
        stock = sim.main.Item(sim.obj[nit - 1])
        if stock == 0:
            sim.obj.pop(nit - 1)
            if len(sim.obj) == 0:
                print("Ya no quedan más consumibles!!!" + "\n")
                prep = True
        elif stock != "Fake":
            sim.obj[nit - 1].stock -= 1
daño = sim.tests[0].Evaluación(main)
sim.main.Restaurar(estado)
if daño == False:
    juego = False
elif daño != True:
    sim.main.life += daño
if juego == True:
    print("Ahora debes prepararte para la siguiente evaluación" + "\n")
    if len(sim.obj) == 0:
        print("No quedan consumibles, ingresa cualquier número para comenzar la evaluación")
        nit = input()
        prep = True
    else:
        print("A continuación encontrarás los consumibles disponibles")
        print("Ingresa el número asociado para utilizarlos")
        print("Cuando quieras comenzar la evaluación ingresa -1" + "\n")
        estado = sim.main.Estado()
        prep = False
        while prep == False:
            sim.Mostrar_Items()
            nit = int(input())
            if nit == -1:
                prep = True
            elif nit not in range(1, len(sim.obj) + 1):
                print("Debes ingresar un número del 1 al", len(sim.obj), "!!!")
            else:
                stock = sim.main.Item(sim.obj[nit - 1])
                if stock == 0:
                    sim.obj.pop(nit - 1)
                    if len(sim.obj) == 0:
                        print("Ya no quedan más consumibles!!!" + "\n")
                        prep = True
                elif stock != "Fake":
                    sim.obj[nit - 1].stock -= 1
        daño = sim.tests[1].Evaluación(main)
        sim.main.Restaurar(estado)
        if daño == False:
            juego = False
        elif daño != True:
            sim.main.life += daño
if juego == True:
    print("Sólo queda prepararse para la última evaluación!!!" + "\n")
    if len(sim.obj) == 0:
        print("No quedan consumibles, ingresa cualquier número para comenzar la evaluación")
        nit = input()
        prep = True
    else:
        print("A continuación encontrarás los consumibles disponibles")
        print("Ingresa el número asociado para utilizarlos")
        print("Cuando quieras comenzar la evaluación ingresa -1" + "\n")
        estado = sim.main.Estado()
        prep = False
        while prep == False:
            sim.Mostrar_Items()
            nit = int(input())
            if nit == -1:
                prep = True
            elif nit not in range(1, len(sim.obj) + 1):
                print("Debes ingresar un número del 1 al", len(sim.obj), "!!!")
            else:
                stock = sim.main.Item(sim.obj[nit - 1])
                if stock == 0:
                    sim.obj.pop(nit - 1)
                    if len(sim.obj) == 0:
                        print("Ya no quedan más consumibles!!!" + "\n")
                        prep = True
                elif stock != "Fake":
                    sim.obj[nit - 1].stock -= 1
        daño = sim.tests[2].Evaluación(main)
        sim.main.Restaurar(estado)
        if daño == False:
            juego = False
        elif daño != True:
            sim.main.life += daño
if juego == True:
    print("Felicidades!!!, has aprobado el duro semestre de universidad" + "\n")
    print("A continuación se muestran tus estadísticas:" + "\n")
    sim.main.Final(sim.tests)
    out = sim.main.datos
    for i in range (len(out)):
        fix = str(out[i]).replace("[","")
        fix2 = fix.replace("]", "")
        print(fix2)
    print("")
    print("¿Deseas guardar estos datos en un archivo de texto? (Si = 1, No = 0)")
    guardar = False
    while guardar == False:
        option = input()
        if option not in ("1", "0"):
            print("Debes ingresar 1 o 0!!!")
        elif option == "1":
            guardar = True
            nombre = input("Ingresa el nombre con el que deseas guardarlo:")
            texto = open(nombre + ".txt", 'w')
            for i in range(len(out) - 1):
                fix = str(out[i]).replace("[", "")
                fix2 = fix.replace("]", "")
                texto.write(fix2 + "\n")
            fix = str(out[len(out) - 1]).replace("[", "")
            fix2 = fix.replace("]", "")
            texto.write(fix2)
            texto.close()
            print("Archivo guardado con éxito!!!")
            time.sleep(2)
        else:
            guardar = True
    print("Hasta la próxima!!!")
    time.sleep(2)