csv = input()
name = csv[0:(len(csv)-4)]
out = []
medios = []
data = open(csv)
for i in data:
    if i != ("Persona;AnoNac;Actividad,Medio"):
        s = i.replace("\n","")
        add = s.split(";")
        add.pop(0)
        add.pop(0)
        out.append(add)
data.close()
counter = []
for i in ("1","2","3","4","5","6","7"):
    c = 0
    maximo = 0
    smax = ""
    t = []
    for k in range(1,len(out)):
        if out[k][0] == i:
            c += 1
            t.append(out[k][1])
    counter.append(c)
    for h in ("1","2","3","4","5","6","7","8","9","10","11"):
        ct = 0
        for l in range(len(t)):
            if t[l] == h:
                ct += 1
        if ct > maximo:
            maximo = ct
            smax = h
    medios.append(smax)
transporte = []
for i in medios:
    if i == "1":
        transporte.append("Tren")
    elif i == "2":
        transporte.append("MicroBus")
    elif i == "3":
        transporte.append("Metro")
    elif i == "4":
        transporte.append("Taxicolectivo")
    elif i == "5":
        transporte.append("TaxiRadiotaxi")
    elif i == "6":
        transporte.append("Bicicleta")
    elif i == "7":
        transporte.append("Auto")
    elif i == "8":
        transporte.append("Motocicleta")
    elif i == "9":
        transporte.append("Caminata")
    elif i == "10":
        transporte.append("No Viaja")
    elif i == "11":
        transporte.append("Otro")
actividades = ["Trabaja","Estudia","Jubilado","Dueño de casa","Busca trabajo por primera vez","Desempleado","Otro"]
new = open(name+"_final.txt",'w')
for i in range(6):
    new.write("Actividad: "+actividades[i]+"\n"+"Cantidad: "+str(counter[i])+"\n"+"Medio más común: "+transporte[i]+"\n"+"\n")
new.write("Actividad: "+actividades[6]+"\n"+"Cantidad: "+str(counter[6])+"\n"+"Medio más común: "+transporte[6])
new.close()