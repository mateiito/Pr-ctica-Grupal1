# Trabajo Practico - Listas Bidimensionales
# Bautista Cano; Mateo Godoy; Alejo Barrozo; Joaquin Lichtenberg

# EJERCICIO 1: Crear una matriz con numeros consecutivos

filas = 3
columnas = 4
matriz = []
numero = 1

for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(numero)
        numero = numero + 1
    matriz.append(fila)

print("EJERCICIO 1 - Matriz con numeros consecutivos:")
for fila in matriz:
    print(fila)

# EJERCICIO 2: Sumar todos los elementos de la matriz

print("\nEJERCICIO 2 - Suma de todos los elementos:")
suma_total = 0
for fila in matriz:
    for elemento in fila:
        suma_total = suma_total + elemento

print("La suma total es:", suma_total)

# EJERCICIO 3: Sumar cada fila

print("\nEJERCICIO 3 - Suma de cada fila:")
for i in range(len(matriz)):
    suma_fila = 0
    for j in range(len(matriz[i])):
        suma_fila = suma_fila + matriz[i][j]
    print("Suma fila", i+1, "=", suma_fila)

# EJERCICIO 4: Transponer la matriz

print("\nEJERCICIO 4 - Matriz transpuesta:")
transpuesta = []
for j in range(len(matriz[0])):
    fila_transpuesta = []
    for i in range(len(matriz)):
        fila_transpuesta.append(matriz[i][j])
    transpuesta.append(fila_transpuesta)

for fila in transpuesta:
    print(fila)

# EJERCICIO 5: Encontrar el elemento mayor

print("\nEJERCICIO 5 - Elemento mayor:")
mayor = matriz[0][0]
for fila in matriz:
    for elemento in fila:
        if elemento > mayor:
            mayor = elemento

print("El elemento mayor es:", mayor)

# EJERCICIO 6: Multiplicar matriz por un escalar

print("\nEJERCICIO 6 - Multiplicar por escalar:")
escalar = int(input("Ingrese un numero para multiplicar: "))
matriz_mult = []
for i in range(len(matriz)):
    fila = []
    for j in range(len(matriz[i])):
        fila.append(matriz[i][j] * escalar)
    matriz_mult.append(fila)

print("Matriz multiplicada por", escalar, ":")
for fila in matriz_mult:
    print(fila)

# EJERCICIO 7: Extraer diagonal principal

print("\nEJERCICIO 7 - Diagonal principal:")
diagonal = []
for i in range(len(matriz)):
    if i < len(matriz[0]):
        diagonal.append(matriz[i][i])

print("Diagonal:", diagonal)

# EJERCICIO 8: Matriz identidad

print("\nEJERCICIO 8 - Matriz identidad:")
n = int(input("Tamaño de la matriz identidad: "))
identidad = []
for i in range(n):
    fila = []
    for j in range(n):
        if i == j:
            fila.append(1)
        else:
            fila.append(0)
    identidad.append(fila)

for fila in identidad:
    print(fila)

# EJERCICIO 9: Matriz identidad inversa

print("\nEJERCICIO 9 - Matriz identidad inversa:")
n = int(input("Tamaño de la matriz: "))
identidad_inversa = []
for i in range(n):
    fila = []
    for j in range(n):
        if i + j == n - 1:
            fila.append(1)
        else:
            fila.append(0)
    identidad_inversa.append(fila)

for fila in identidad_inversa:
    print(fila)

# EJERCICIO 10: Verificar si matriz es simetrica

print("\nEJERCICIO 10 - Verificar si es simetrica:")
# Hacemos la transpuesta
trans = []
for j in range(len(matriz[0])):
    fila = []
    for i in range(len(matriz)):
        fila.append(matriz[i][j])
    trans.append(fila)

# Comparamos
if matriz == trans:
    print("La matriz SI es simetrica")
else:
    print("La matriz NO es simetrica")

# EJERCICIO 11: Rotar matriz 90 grados

print("\nEJERCICIO 11 - Rotar matriz 90 grados:")
rotada = []
for j in range(len(matriz[0])):
    fila = []
    for i in range(len(matriz)-1, -1, -1):
        fila.append(matriz[i][j])
    rotada.append(fila)

print("Matriz rotada:")
for fila in rotada:
    print(fila)
