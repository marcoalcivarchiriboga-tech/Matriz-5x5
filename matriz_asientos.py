#crear una matriz 3x4 para representar los asientos
asientos = [[0 for _ in range (4) ]for _ in range (3)] 

#pedir al usuario que elija la fila y columna para reservar
f = int(input("ingrese fila (0 a 2):"))
c = int(input("ingrese columna (0 a 3):"))

#Marcar el asiento como reservado 
asientos [f][c] = 1

#Mostrar el estado de la sala 
print("Estado de la sala:")
for i in range(3):
    for j in range(4):
        print(asientos[i][j], end="") 
    print() #hace que se imprima en forma de matriz

