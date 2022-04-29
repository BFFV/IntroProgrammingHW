csv = input()
name = csv[0:(len(csv)-4)]
filas = []
data = open(csv)
col = data.readline()
categorias = col.split(";")
for i in range(len(categorias)):
    if categorias[i] == "Persona":
        p = i
    elif categorias[i] == "AnoNac":
        y = i
    elif categorias[i] == "Actividad":
        a = i
    elif categorias[i] == "Medio":
        m = i
for i in data:
    k = i.replace("\n","")
    filas.append(k.split(";"))
largo = len(filas[0])
data.close()
nuevo = open(name+"_filtrado.csv",'w')
nuevo.write("Persona;AnoNac;Actividad;Medio\n")
for i in range(len(filas)):
    add = []
    for j in range(largo):
        if (str(j) in (str(p),str(y),str(a),str(m))) is True:
            add.append(filas[i][j])
    if i == (len(filas)-1):
        nuevo.write((";".join(add)))
    else:
        nuevo.write((";".join(add))+"\n")
nuevo.close()