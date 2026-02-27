#crear la matriz vacia 
matriz = [[0 for _ in range (5)] for _ in range (5)]
#llenar la matriz con datos ingresados por el usuario 
for i in range (5):
    for j in range(5):
        valor = int(input (f"ingrese el valor para la posicion [{i}][{j}]: "))
        matriz [i][j] = valor 

#mostrar la matriz generada 
print("\nMatriz Ingresada: ")
for i in range (5):
    for j in range (5):
        print(matriz[i][j], end="")
    print()
    