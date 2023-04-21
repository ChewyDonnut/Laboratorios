fila=int(input("ingrese la cantidad de filas"))
columnas=(int(input("ingrese la cantidad de columnas")))
matriz=[]
for i in range(fila):
    matriz.append(int(input("ingrese dato ¿cual? no sé,\n")))
    for a in range(0,columnas):
        matriz.append(int(input("a\n")))
        print(end=" ")
print(" ")
print(matriz)