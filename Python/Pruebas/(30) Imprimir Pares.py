# Imprimir solo los pares de un rango de números

n = int(input("Ingrese un numero: "))
for i in range(1, n+1):
    if i % 2 == 0:
        print(i)
