txt = input()
actividades = []
data = open(txt)
for i in data:
    l = i.split(" ")
    accion = l[2][0]
    actividades.append(accion)
data.close()
Trabaja = 0
Estudia = 0
Jubilado = 0
Dueño_de_casa = 0
Busca_trabajo_por_primera_vez = 0
Desempleado = 0
Otro = 0
for i in actividades:
    if i == "1":
        Trabaja += 1
    elif i == "2":
        Estudia += 1
    elif i == "3":
        Jubilado += 1
    elif i == "4":
        Dueño_de_casa += 1
    elif i == "5":
        Busca_trabajo_por_primera_vez += 1
    elif i == "6":
        Desempleado += 1
    elif i == "7":
        Otro += 1
print("Trabaja: "+str(Trabaja))
print("Estudia: "+str(Estudia))
print("Jubilado: "+str(Jubilado))
print("Dueño de casa: "+str(Dueño_de_casa))
print("Busca trabajo por primera vez: "+str(Busca_trabajo_por_primera_vez))
print("Desempleado: "+str(Desempleado))
print("Otro: "+str(Otro))
#python tester.py p1.py p2.py p3.py