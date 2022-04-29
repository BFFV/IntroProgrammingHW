import random

from Tarea_1 import *

root = tk.Tk()
root.geometry('{}x{}'.format("550", "650"))
app = Application(master=root)

    
def turno(): #turnos 
    if (app.obtener_apuesta() == -1000):                      #Despedida
        app.mostrar_mensaje("Hasta Luego!!! (Presione Sig.Turno Para Salir)")
        app.poner_apuesta(-100)
        app.mostrar_ventana(True)
    elif (app.obtener_apuesta() == -100):             #Fin del Juego
        app.cerrar_ventana()    
    elif (app.obtener_apuesta() == -2):          #Caso de Empate
        for h in range(1,3):
            for i in range(5):
                for k in range(5):
                    app.marcar_numero(i, k, False, h)
        app.mostrar_ventana(False)
        Repetir = input()
        if (Repetir == ("SI")):
            app.poner_apuesta(0)
            app.mostrar_mensaje("Presione Sig.Turno Para Ingresar La Nueva Apuesta")
            app.mostrar_ventana(True)
        elif (Repetir == ("NO")):
            if (app.preguntar_monto(1) > app.preguntar_monto(2)):
                app.poner_apuesta(-1000)
                app.mostrar_mensaje("El Ganador DEFINITIVO Es El Jugador 1!!! (Presione Sig.Turno)")
            elif (app.preguntar_monto(2) > app.preguntar_monto(1)):
                app.poner_apuesta(-1000)
                app.mostrar_mensaje("El Ganador DEFINITIVO Es El Jugador 2!!! (Presione Sig.Turno)")
            elif (app.preguntar_monto(1) == app.preguntar_monto(2)):
                app.poner_apuesta(-1000)
                app.mostrar_mensaje("No Hubo Un Ganador DEFINITIVO (Presione Sig.Turno)")    
            app.mostrar_ventana(True)
        else:
            app.mostrar_mensaje("Por Favor Ingrese Su Respuesta En Mayúscula (Presione Sig.Turno)")
            app.mostrar_ventana(True)
    elif (app.obtener_apuesta() == -1):                  #Caso de Victoria
        for h in range(1,3):
            for i in range(5):
                for k in range(5):
                    app.marcar_numero(i, k, False, h)
        app.mostrar_ventana(False)
        Repetir = input()
        if (Repetir == "SI"):
            app.poner_apuesta(0)
            app.mostrar_mensaje("Presione Sig.Turno Para Ingresar La Nueva Apuesta")
            app.mostrar_ventana(True)
        elif (Repetir == ("NO")):
            if (app.preguntar_monto(1) > app.preguntar_monto(2)):
                app.poner_apuesta(-1000)
                app.mostrar_mensaje("El Ganador DEFINITIVO Es El Jugador 1!!! (Presione Sig.Turno)")
            elif (app.preguntar_monto(2) > app.preguntar_monto(1)):
                app.poner_apuesta(-1000)
                app.mostrar_mensaje("El Ganador DEFINITIVO Es El Jugador 2!!! (Presione Sig.Turno)")
            elif (app.preguntar_monto(1) == app.preguntar_monto(2)):
                app.poner_apuesta(-1000)
                app.mostrar_mensaje("No Hubo Un Ganador DEFINITIVO (Presione Sig.Turno)")    
            app.mostrar_ventana(True)
        else:
            app.mostrar_mensaje("Debe Ingresar Su Respuesta En Mayúscula (Presione Sig.Turno)")
            app.mostrar_ventana(True)   
    elif (app.preguntar_monto(1) == "?"):              #Comienzo del Juego Inicial
        app.mostrar_ventana(False)
        monto = int(input())
        app.mostrar_dinero(1, monto)
        app.mostrar_dinero(2, monto)
        app.mostrar_ventana(True)
        app.mostrar_mensaje("Presione Sig.Turno Para Ingresar Su Apuesta")
    elif (app.obtener_apuesta() == 0):                  #Comienzo de Juego
        app.mostrar_ventana(False)
        apuesta = int(input())
        if (apuesta > app.preguntar_monto(1) or apuesta > app.preguntar_monto(2)):
            app.mostrar_mensaje("No Tiene El Monto Suficiente! (Presione Sig.Turno Para Cambiar La Apuesta)")
            app.mostrar_ventana(True)
        elif (apuesta <= 0):
            app.mostrar_mensaje("Ésta Apuesta No Es Válida! (Presione Sig.Turno Para Cambiar La Apuesta)")
            app.mostrar_ventana(True)
        else:
            app.poner_apuesta(apuesta)
            app.mostrar_mensaje("Los Cartones Están Listos!, Presione Sig.Turno Para Comenzar El Bingo!!!")
            app.mostrar_dinero(1, app.preguntar_monto(1)- apuesta)
            app.mostrar_dinero(2, app.preguntar_monto(2)- apuesta)                                    
            for i in range(5):
                for k in range(5):      #generar cartón 1, i = filas, k = columnas, N = 0 (número que falta)
                    a = (k*20)+ 1
                    b = a + 19                       
                    N = 0
                    while (N == 0):
                        num = random.randint(a,b)
                        if (app.agregar(num) == True):
                            app.colocar_numero(i, k, num, 1)
                            N = 1
            app.reiniciar_contador()                
            for i in range(5):
                for k in range(5):      #generar cartón 2
                    a = (k*20)+ 1
                    b = a + 19                       
                    N = 0
                    while (N == 0):
                        num = random.randint(a,b)
                        if (app.agregar(num) == True):
                            app.colocar_numero(i, k, num, 2)
                            N = 1                 
            app.mostrar_ventana(True)
            app.reiniciar_contador()
    elif (app.obtener_apuesta()> 0):
        B = 0
        while (B == 0):                                                          #Bolas de Números
            Bola = random.randint(1,100)
            NBola = str(Bola)
            if (app.agregar(Bola) == True):
                app.mostrar_mensaje("Ha Salido El Número "+ NBola +"!!!")
                B = 1
                for i in range(5):
                    for k in range(5):
                        if (app.obtener_numero(i, k, 1)== Bola):
                            app.marcar_numero(i, k, True, 1)
                for i in range(5):
                    for k in range(5):
                        if (app.obtener_numero(i, k, 2)== Bola):
                            app.marcar_numero(i, k, True, 2)
                Diagonal = 0
                Ganador1 = 0
                Ganador2 = 0
                pD = 1
                pY = 2
                pF = 3
                for i in range(5):                                 #Formar Diagonal
                    if (app.esta_marcado(i, i, 1) == True):
                        Diagonal+= 1
                if (Diagonal == 5):
                    Ganador1 = pD
                Diagonal = 0
                for i in range(5):
                    if (app.esta_marcado(i, i, 2) == True):
                        Diagonal+= 1
                if (Diagonal == 5):
                    Ganador2 = pD
                Y = 0                                              #Formar Y
                for i in range(2):
                    if (app.esta_marcado(i, 4-i, 1) == True):
                        Y+= 1
                    if (app.esta_marcado(i, i, 1) == True):
                        Y+= 1    
                for i in range(2,5):
                    if (app.esta_marcado(i, 2, 1) == True):
                        Y+= 1
                if (Y == 7):
                    Ganador1 = pY
                Y = 0
                for i in range(2):
                    if (app.esta_marcado(i, 4-i, 2) == True):
                        Y+= 1
                    if (app.esta_marcado(i, i, 2) == True):
                        Y+= 1    
                for i in range(2,5):
                    if (app.esta_marcado(i, 2, 2) == True):
                        Y+= 1
                if (Y == 7):
                    Ganador2 = pY
                Full = 0                                              #Formar Cartón Completo
                for i in range(5):
                    for k in range(5):
                        if (app.esta_marcado(i, k, 1) == True):
                            Full+= 1
                if (Full == 25):
                    Ganador1 = pF
                Full = 0
                for i in range(5):
                    for k in range(5):
                        if (app.esta_marcado(i, k, 2) == True):
                            Full+= 1
                if (Full == 25):
                    Ganador2 = pF
                if (Ganador1 > Ganador2):                                  #Determinar Ganador
                    app.reiniciar_contador()
                    Monto1 = (app.obtener_apuesta())*2 + app.preguntar_monto(1)
                    app.mostrar_dinero(1, Monto1)
                    if (app.preguntar_monto(2) == 0):
                        app.mostrar_mensaje("El Ganador DEFINITIVO Es El Jugador 1!!! (Presione Sig.Turno)")
                        app.poner_apuesta(-1000)
                    else:
                        app.poner_apuesta(-1)
                        app.mostrar_mensaje("El Ganador Es El Jugador 1!!!, ¿Desea Continuar Jugando?(SI o NO)")
                elif (Ganador2 > Ganador1):
                    app.reiniciar_contador()
                    Monto2 = (app.obtener_apuesta())*2 + app.preguntar_monto(2)
                    app.mostrar_dinero(2, Monto2)
                    if (app.preguntar_monto(1) == 0):
                        app.mostrar_mensaje("El Ganador DEFINITIVO Es El Jugador 2!!! (Presione Sig.Turno)")
                        app.poner_apuesta(-1000)
                    else:
                        app.poner_apuesta(-1)
                        app.mostrar_mensaje("El Ganador Es El Jugador 2!!!, ¿Desea Continuar Jugando?(SI o NO)")
                elif (Ganador2 == Ganador1 and Ganador1 > 0 and Ganador2 > 0):
                    app.reiniciar_contador()
                    Monto1 = app.obtener_apuesta() + app.preguntar_monto(1)
                    Monto2 = app.obtener_apuesta() + app.preguntar_monto(2)
                    app.mostrar_dinero(1, Monto1)
                    app.mostrar_dinero(2, Monto2)
                    app.poner_apuesta(-2)
                    app.mostrar_mensaje("Ha Ocurrido Un Empate, ¿Desea Continuar Jugando?(SI o NO)")
    pass 

# Programa(inicio)
app.mostrar_ventana(True)
app.mostrar_mensaje("Bienvenido!!!, Para Comenzar Presione Sig.Turno e Ingrese el Monto Inicial")
app.mostrar_dinero(1,"?")
app.mostrar_dinero(2,"??")

# ESTO NO SE TOCA
app.button.config(command=turno)
app.mainloop()
