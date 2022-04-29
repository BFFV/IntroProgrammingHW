import time
import os.path
def tablero_nuevo():
    tablero = [["G","G","G","G","G"],["G","G","G","G","G"],["G","N","C","N","G"],["N","N","N","N","N"],["N","N","N","N","N"]]
    return tablero
def mostrar_tablero(tablero):
    print("")
    print("-".join(tablero[0]))
    print("|\\|/|\\|/|")
    print("-".join(tablero[1]))
    print("|/|\\|/|\\|")
    print("-".join(tablero[2]))
    print("|\\|/|\\|/|")
    print("-".join(tablero[3]))
    print("|/|\\|/|\\|")
    print("-".join(tablero[4]))
    print("")
def validar_gallina(x1,y1,x2,y2,tablero):
    if (x1 in (0,1,2,3,4)) and (y1 in (0,1,2,3,4)) and (x2 in (0,1,2,3,4)) and (y2 in (0,1,2,3,4)) is True:
        if (str(x1)+str(y1))==(str(x2)+str(y2)):
            return False
        elif tablero[y1][x1]!= "G":
            return False
        else:
            if ((y1 in (0,2,4)) and (x1 in (0,2,4))) or ((y1 in (1,3)) and (x1 in (1,3))) is True:  #diagonal
                if(((y2 in (y1-1,y1,y1+1)) and (x2 in (x1-1,x1,x1+1)) is True)):
                    if (tablero[y2][x2])=="N":
                        return True
                    else:
                        return False
                else:
                    return False
            else: #recta
                if ((y2 in (y1-1,y1+1)) and (x2 == x1)) or ((y2 == y1) and (x2 in (x1-1,x1+1))) is True:
                    if (tablero[y2][x2])=="N":
                        return True
                    else:
                        return False
                else:
                    return False
    else:
        return False
def turno_gallina(nombre,tablero,data):
    listo = 0
    while listo == 0:
        print("Es tu turno", nombre, ", ¿Cuál es tu jugada (x1,y1,x2,y2)?")
        print("x = Ubicación Horizontal (0 a 4), y = Ubicación Vertical (0 a 4), 1 = Inicial, 2 = Final")
        print("¿O deseas guardar la partida y salir del juego (G)?")
        print("¿O deseas salir sin guardar (S)?")
        option = input()
        if (option.upper()) == "G":
            listo = 2
        elif (option.upper()) == "S":
            listo = 3
        else:
            if len(option)>= 7:
                if (option[0] and option[2] and option[4] and option[6] in ("0", "1", "2", "3", "4")) is True and (
                        option[1] and option[3] and option[5] in (",")) is True:
                    jugada = option.split(",")
                    x1 = int(jugada[0])
                    y1 = int(jugada[1])
                    x2 = int(jugada[2])
                    y2 = int(jugada[3])
                    if validar_gallina(x1, y1, x2, y2, tablero) is True:
                        tablero[y1][x1] = "N"
                        tablero[y2][x2] = "G"
                        listo = 1
                        data.append("G," + str(x1) + "," + str(y1) + "," + str(x2) + "," + str(y2))
                    else:
                        print("La jugada no es válida!!!, se repite el turno")
                else:
                    print("La jugada no es válida!!!, se repite el turno")
            else:
                print("La jugada no es válida!!!, se repite el turno")
    if listo == 1:
        return tablero,data
    elif listo == 2:
        return "save",data
    else:
        return "quit",data
def validar_coyote(x1,y1,x2,y2,tablero):
    if (x1 in (0,1,2,3,4)) and (y1 in (0,1,2,3,4)) and (x2 in (0,1,2,3,4)) and (y2 in (0,1,2,3,4)) is True:
        if (str(x1)+str(y1))==(str(x2)+str(y2)):
            return False,0,0,0
        elif tablero[y1][x1]!= "C":
            return False,0,0,0
        else:
            if ((y1 in (0,2,4)) and (x1 in (0,2,4))) or ((y1 in (1,3)) and (x1 in (1,3))) is True:  #diagonal
                if(((y2 in (y1-1,y1,y1+1)) and (x2 in (x1-1,x1,x1+1)) is True)): #moverse
                    if (tablero[y2][x2])=="N":
                        return True,"mover",0,0
                    else:
                        return False,0,0,0
                elif (y2 == (y1-2)) and (x2 == (x1-2)):     #comer
                    if ((tablero[y2][x2])=="N") and ((tablero[y1-1][x1-1])=="G"):
                        return True,"comer",(y1-1),(x1-1)
                    else:
                        return False,0,0,0
                elif (y2 == (y1-2)) and (x2 == x1):     #comer
                    if ((tablero[y2][x2])=="N") and ((tablero[y1-1][x1])=="G"):
                        return True,"comer",(y1-1),x1
                    else:
                        return False,0,0,0
                elif (y2 == (y1-2)) and (x2 == (x1+2)):     #comer
                    if ((tablero[y2][x2])=="N") and ((tablero[y1-1][x1+1])=="G"):
                        return True,"comer",(y1-1),(x1+1)
                    else:
                        return False,0,0,0
                elif (y2 == (y1+2)) and (x2 == (x1-2)):     #comer
                    if ((tablero[y2][x2])=="N") and ((tablero[y1+1][x1-1])=="G"):
                        return True,"comer",(y1+1),(x1-1)
                    else:
                        return False,0,0,0
                elif (y2 == (y1+2)) and (x2 == x1):     #comer
                    if ((tablero[y2][x2])=="N") and ((tablero[y1+1][x1])=="G"):
                        return True,"comer",(y1+1),x1
                    else:
                        return False,0,0,0
                elif (y2 == (y1+2)) and (x2 == (x1+2)):     #comer
                    if ((tablero[y2][x2])=="N") and ((tablero[y1+1][x1+1])=="G"):
                        return True,"comer",(y1+1),(x1+1)
                    else:
                        return False,0,0,0
                elif (y2 == y1) and (x2 == (x1-2)):     #comer
                    if ((tablero[y2][x2])=="N") and ((tablero[y1][x1-1])=="G"):
                        return True,"comer",y1,(x1-1)
                    else:
                        return False,0,0,0
                elif (y2 == y1) and (x2 == (x1+2)):     #comer
                    if ((tablero[y2][x2])=="N") and ((tablero[y1][x1+1])=="G"):
                        return True,"comer",y1,(x1+1)
                    else:
                        return False,0,0,0
                else:
                    return False,0,0,0
            else: #recta
                if ((y2 in (y1-1,y1+1)) and (x2 == x1)) or ((y2 == y1) and (x2 in (x1-1,x1+1))) is True: #moverse
                    if (tablero[y2][x2])=="N":
                        return True,"mover",0,0
                    else:
                        return False,0,0,0
                elif (y2 == y1) and (x2 == (x1-2)):     #comer
                    if ((tablero[y2][x2])=="N") and ((tablero[y1][x1-1])=="G"):
                        return True,"comer",y1,(x1-1)
                    else:
                        return False,0,0,0
                elif (y2 == y1) and (x2 == (x1+2)):     #comer
                    if ((tablero[y2][x2])=="N") and ((tablero[y1][x1+1])=="G"):
                        return True,"comer",y1,(x1+1)
                    else:
                        return False,0,0,0
                elif (y2 == (y1-2)) and (x2 == x1):     #comer
                    if ((tablero[y2][x2])=="N") and ((tablero[y1-1][x1])=="G"):
                        return True,"comer",(y1-1),x1
                    else:
                        return False,0,0,0
                elif (y2 == (y1+2)) and (x2 == x1):     #comer
                    if ((tablero[y2][x2])=="N") and ((tablero[y1+1][x1])=="G"):
                        return True,"comer",(y1+1),x1
                    else:
                        return False,0,0,0
                else:
                    return False,0,0,0
    else:
        return False,0,0,0
def turno_coyote(nombre,tablero,data):
    listo = 0
    while listo == 0:
        print("Es tu turno", nombre, ", ¿Cuál es tu jugada (x1,y1,x2,y2)?")
        print("x = Ubicación Horizontal (0 a 4), y = Ubicación Vertical (0 a 4), 1 = Inicial, 2 = Final")
        print("¿O deseas guardar la partida y salir del juego (G)?")
        print("¿O deseas salir sin guardar (S)?")
        option = input()
        if (option.upper()) == "G":
            listo = 2
        elif (option.upper()) == "S":
            listo = 3
        else:
            if len(option) >= 7:
                if (option[0] and option[2] and option[4] and option[6] in ("0", "1", "2", "3", "4")) is True and (
                                option[1] and option[3] and option[5] in (",")) is True:
                    jugada = option.split(",")
                    x1 = int(jugada[0])
                    y1 = int(jugada[1])
                    x2 = int(jugada[2])
                    y2 = int(jugada[3])
                    valido, accion, Gy, Gx = validar_coyote(x1, y1, x2, y2, tablero)
                    if valido == True:
                        if accion == "comer":
                            tablero[y1][x1] = "N"
                            tablero[y2][x2] = "C"
                            tablero[Gy][Gx] = "N"
                            listo = 1
                            data.append("C," + str(x1) + "," + str(y1) + "," + str(x2) + "," + str(y2))
                        else:
                            tablero[y1][x1] = "N"
                            tablero[y2][x2] = "C"
                            listo = 1
                            data.append("C," + str(x1) + "," + str(y1) + "," + str(x2) + "," + str(y2))
                    else:
                        print("La jugada no es válida!!!, se repite el turno")
                else:
                    print("La jugada no es válida!!!, se repite el turno")
            else:
                print("La jugada no es válida!!!, se repite el turno")
    if (listo == 1) and (accion == "comer"):
        return tablero,"comida",data
    elif (listo == 1) and (accion == "mover"):
        return tablero,"mover",data
    elif listo == 2:
        return "save",0,data
    else:
        return "quit",0,data
def combo_coyote(tablero):
    combo = False
    for h in range(5):
        for i in range(5):
            for j in range(5):
                for k in range(5):
                    valido, accion, Gy, Gx = validar_coyote(h, i, j, k, tablero)
                    if (valido == True) and (accion == "comer"):
                        combo = True
    return combo
def turno_combo(tablero,data):
    listo = 0
    while listo == 0:
        print("El Coyote aún puede seguir comiendo en este turno!!!(x1,y1,x2,y2)")
        print("x = Ubicación Horizontal (0 a 4), y = Ubicación Vertical (0 a 4), 1 = Inicial, 2 = Final")
        option = input()
        if len(option) >= 7:
            if (option[0] and option[2] and option[4] and option[6] in ("0", "1", "2", "3", "4")) is True and (
                            option[1] and option[3] and option[5] in (",")) is True:
                jugada = option.split(",")
                x1 = int(jugada[0])
                y1 = int(jugada[1])
                x2 = int(jugada[2])
                y2 = int(jugada[3])
                valido, Gy, Gx = validar_combo(x1, y1, x2, y2, tablero)
                if valido == True:
                    tablero[y1][x1] = "N"
                    tablero[y2][x2] = "C"
                    tablero[Gy][Gx] = "N"
                    listo = 1
                    data.append("C," + str(x1) + "," + str(y1) + "," + str(x2) + "," + str(y2))
                else:
                    print("La jugada no es válida!!!, debes seguir comiendo gallinas")
            else:
                print("La jugada no es válida!!!, se repite el turno")
        else:
            print("La jugada no es válida!!!, se repite el turno")
    return tablero, "comida",data
def validar_combo(x1,y1,x2,y2,tablero):
    if (x1 in (0,1,2,3,4)) and (y1 in (0,1,2,3,4)) and (x2 in (0,1,2,3,4)) and (y2 in (0,1,2,3,4)) is True:
        if (str(x1)+str(y1))==(str(x2)+str(y2)):
            return False,0,0
        elif tablero[y1][x1]!= "C":
            return False,0,0
        else:
            if ((y1 in (0,2,4)) and (x1 in (0,2,4))) or ((y1 in (1,3)) and (x1 in (1,3))) is True:  #diagonal
                if (y2 == (y1-2)) and (x2 == (x1-2)):     #comer
                    if ((tablero[y2][x2])=="N") and ((tablero[y1-1][x1-1])=="G"):
                        return True,(y1-1),(x1-1)
                    else:
                        return False,0,0
                elif (y2 == (y1-2)) and (x2 == x1):     #comer
                    if ((tablero[y2][x2])=="N") and ((tablero[y1-1][x1])=="G"):
                        return True,(y1-1),x1
                    else:
                        return False,0,0
                elif (y2 == (y1-2)) and (x2 == (x1+2)):     #comer
                    if ((tablero[y2][x2])=="N") and ((tablero[y1-1][x1+1])=="G"):
                        return True,(y1-1),(x1+1)
                    else:
                        return False,0,0
                elif (y2 == (y1+2)) and (x2 == (x1-2)):     #comer
                    if ((tablero[y2][x2])=="N") and ((tablero[y1+1][x1-1])=="G"):
                        return True,(y1+1),(x1-1)
                    else:
                        return False,0,0
                elif (y2 == (y1+2)) and (x2 == x1):     #comer
                    if ((tablero[y2][x2])=="N") and ((tablero[y1+1][x1])=="G"):
                        return True,(y1+1),x1
                    else:
                        return False,0,0
                elif (y2 == (y1+2)) and (x2 == (x1+2)):     #comer
                    if ((tablero[y2][x2])=="N") and ((tablero[y1+1][x1+1])=="G"):
                        return True,(y1+1),(x1+1)
                    else:
                        return False,0,0
                elif (y2 == y1) and (x2 == (x1-2)):     #comer
                    if ((tablero[y2][x2])=="N") and ((tablero[y1][x1-1])=="G"):
                        return True,y1,(x1-1)
                    else:
                        return False,0,0
                elif (y2 == y1) and (x2 == (x1+2)):     #comer
                    if ((tablero[y2][x2])=="N") and ((tablero[y1][x1+1])=="G"):
                        return True,y1,(x1+1)
                    else:
                        return False,0,0
                else:
                    return False,0,0
            else: #recta
                if (y2 == y1) and (x2 == (x1-2)):     #comer
                    if ((tablero[y2][x2])=="N") and ((tablero[y1][x1-1])=="G"):
                        return True,y1,(x1-1)
                    else:
                        return False,0,0
                elif (y2 == y1) and (x2 == (x1+2)):     #comer
                    if ((tablero[y2][x2])=="N") and ((tablero[y1][x1+1])=="G"):
                        return True,y1,(x1+1)
                    else:
                        return False,0,0
                elif (y2 == (y1-2)) and (x2 == x1):     #comer
                    if ((tablero[y2][x2])=="N") and ((tablero[y1-1][x1])=="G"):
                        return True,(y1-1),x1
                    else:
                        return False,0,0
                elif (y2 == (y1+2)) and (x2 == x1):     #comer
                    if ((tablero[y2][x2])=="N") and ((tablero[y1+1][x1])=="G"):
                        return True,(y1+1),x1
                    else:
                        return False,0,0
                else:
                    return False,0,0
    else:
        return False,0,0
def encierro(tablero):
    corner = True
    for h in range(5):
        for i in range(5):
            for j in range(5):
                for k in range(5):
                    valido, accion, Gy, Gx = validar_coyote(h, i, j, k, tablero)
                    if (valido == True):
                        corner = False
    return corner
def guardar_partida(data):
    print("¿Con qué nombre desea Guardar la partida?")
    save_name = input()
    savefile = open(save_name + ".txt", 'w')
    for i in range(len(data)):
        savefile.write(data[i] + "\n")
    savefile.close()
    print("Partida Guardada con Éxito!!!")
def cargar_partida():
    data = []
    path = False
    while path == False:
        print("¿Cuál es el Nombre de la Partida? (sin el .txt)")
        name = input() + ".txt"
        if os.path.exists(name):
            path = True
        else:
            print("No existe ninguna partida de nombre", name, "!!!")
    load = open(name)
    for i in load:
        data.append(i.replace("\n",""))
    names = (data[0].split(","))
    Cname = names[0]
    Gname = names[1]
    load.close()
    print("Partida cargada con Éxito!!!")
    return data, Cname, Gname
def historial(data):
    tablero = tablero_nuevo()
    print("")
    print("Jugadores:",data[0])
    print("")
    mostrar_tablero(tablero)
    G = 0
    for i in range(1,len(data)):
        jugada = data[i]
        print("")
        print("Jugada:"+jugada)
        if jugada[0] == "G":
            turn = jugada[2:]
            t = turn.split(",")
            tablero[int(t[1])][int(t[0])] = "N"
            tablero[int(t[3])][int(t[2])] = "G"
            print("")
            mostrar_tablero(tablero)
        else:
            turn = jugada[2:]
            t = turn.split(",")
            valido, accion, Gy, Gx = validar_coyote(int(t[0]), int(t[1]), int(t[2]), int(t[3]), tablero)
            if accion == "comer":
                tablero[int(t[1])][int(t[0])] = "N"
                tablero[int(t[3])][int(t[2])] = "C"
                tablero[Gy][Gx] = "N"
                G+=1
            else:
                tablero[int(t[1])][int(t[0])] = "N"
                tablero[int(t[3])][int(t[2])] = "C"
            print("")
            mostrar_tablero(tablero)
    return tablero, G

juego = True
terminado = False
data = []
print("Bienvenido al juego del Coyote y las Gallinas!!!")
print("¿Deseas Cargar una Partida (1) o Crear una Nueva (2)?")
bug = True
while bug == True:
    option = input()
    if (option in ("1","2")) is True:
        bug = False
    else:
        print("Debes presionar 1 o 2!!!")
option = int(option)
while juego == True:
    if option == 1:
        tablero = "load"
    else:
        terminado = False
        if data == []:
            continuar = False
            tablero = tablero_nuevo()
            print("¡Perfecto!, Ingresa el nombre del jugador que controlará al Coyote:")
            Cname = input()
            print("Ahora Ingresa el nombre del jugador que controlará a las Gallinas:")
            Gname = Cname
            while Gname == Cname:
                Gname = input()
                if (Gname == Cname):
                    print("No se puede repetir el nombre del primer jugador!!!")
            data = [Cname + "," + Gname]
            print("Todo Listo, ¡¡¡Comencemos!!!")
            mostrar_tablero(tablero)
            Gdevoradas = 0
        fin = False
        while fin == False:
            if continuar == False:
                tablero, data = turno_gallina(Gname, tablero, data)
                if (tablero == "save") or (tablero == "quit"):
                    fin = True
                else:
                    mostrar_tablero(tablero)
                    if encierro(tablero) == True:
                        tablero = "Gwin"
                        fin = True
                    else:
                        tablero, accion, data = turno_coyote(Cname, tablero, data)
                        if (tablero == "save") or (tablero == "quit"):
                            fin = True
                        else:
                            combo = True
                            while combo == True:
                                if accion == "comida":
                                    Gdevoradas += 1
                                    mostrar_tablero(tablero)
                                    print("El Coyote ha devorado una Gallina!!!")
                                    combo = combo_coyote(tablero)
                                    if combo == True:
                                        tablero, accion, data = turno_combo(tablero, data)
                                else:
                                    combo = False
                                    mostrar_tablero(tablero)
                            if Gdevoradas >= 2:
                                tablero = "Cwin"
                                fin = True
            else:
                continuar = False
                last = data[len(data)-1]
                if last[0] == "G":
                    if encierro(tablero) == True:
                        tablero = "Gwin"
                        fin = True
                    else:
                        tablero, accion, data = turno_coyote(Cname, tablero, data)
                        if (tablero == "save") or (tablero == "quit"):
                            fin = True
                        else:
                            combo = True
                            while combo == True:
                                if accion == "comida":
                                    Gdevoradas += 1
                                    mostrar_tablero(tablero)
                                    print("El Coyote ha devorado una Gallina!!!")
                                    combo = combo_coyote(tablero)
                                    if combo == True:
                                        tablero, accion, data = turno_combo(tablero, data)
                                else:
                                    combo = False
                                    mostrar_tablero(tablero)
                            if Gdevoradas >= 2:
                                tablero = "Cwin"
                                fin = True
                else:
                    if Gdevoradas >= 2:
                        tablero = "Cwin"
                        fin = True
    if tablero == "Gwin":
        print("Las Gallinas han encerrado al Coyote, ¡¡¡ El ganador es", Gname, "!!!")
        terminado = True
    elif tablero == "Cwin":
        print("El Coyote se ha comido a 2 o más Gallinas, ¡¡¡ El ganador es", Cname, "!!!")
        terminado = True
    elif tablero == "quit":
        print("Hasta la Próxima!!!")
        juego = False
        time.sleep(1)
    elif tablero == "save":
        juego = False
        guardar_partida(data)
        print("Hasta la Próxima!!!")
        time.sleep(2)
    elif tablero == "load":
        data, Cname, Gname = cargar_partida()
        tablero, Gdevoradas = historial(data)
        continuar = True
        option = 2
        terminado = False
    if terminado == True:
        print("¿Desean guardar esta Partida? (1)Si,(2)No")
        savbug = True
        while savbug == True:
            sav = input()
            if (sav in ("1","2")) is True:
                savbug = False
            else:
                print("Debes presionar 1 o 2!!!")
        if sav == "1":
            guardar_partida(data)
        print("¿Desean Cargar una Partida? (1)")
        print("¿O Empezar de Nuevo? (2)")
        print("¿O Salir del Juego? (3)")
        opbug = True
        while opbug == True:
            option = input()
            if (option in ("1", "2", "3")) is True:
                opbug = False
            else:
                print("Debes presionar 1, 2 o 3!!!")
        option = int(option)
        if option == 3:
            print("Hasta la Próxima!!!")
            juego = False
            time.sleep(1)
        else:
            data = []