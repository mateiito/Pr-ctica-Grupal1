#Ejercicio 1: Suma de Elementos Escribe un programa que permita al usuario ingresar una lista de números y calcule la suma de todos los elementos en la lista. 

numeros1 = input("Ingrese una lista de números separados por espacios: ").split()
numeros1 = [float(x) for x in numeros1]
total = sum(numeros1)
print(f"La suma de los elementos en la lista es: {total}")

#Ejercicio 2: Encontrar el Mayor y el Menor Escribe un programa que pida al usuario una lista de números y encuentre el mayor y el menor de ellos. 

numeros2 = input("Ingrese una lista de números separados por espacios: ").split()
numeros2 = [float(x) for x in numeros2]
maximo2 = max(numeros2)
minimo2 = min(numeros2)
print(f"El mayor número en la lista es: {maximo2}")
print(f"El menor número en la lista es: {minimo2}")

#Ejercicio 3: Invertir una Lista Escribe un programa que permita al usuario ingresar una lista y la invierta.

numeros3 = input("Ingrese una lista de números separados por espacios: ").split()
numeros3 = [float(x) for x in numeros3]
numeros3.reverse()
print(f"La lista invertida es: {numeros3}")

#Ejercicio 4: Contar Elementos Pares e Impares Escribe un programa que pida al usuario una lista de números y cuente cuántos de ellos son pares y cuántos son impares. 

numeros4 = input("Ingrese una lista de números separados por espacios: ").split()
numeros4 = [float(x) for x in numeros4]
pares = sum(1 for x in numeros4 if x % 2 == 0)
impares = len(numeros4) - pares
print(f"La cantidad de números pares en la lista es: {pares}")
print(f"La cantidad de números impares en la lista es: {impares}")

#Ejercicio 5: Multiplicar Elementos por un Valor Escribe un programa que multiplique cada elemento de una lista de números por un valor ingresado por el usuario. 

numeros5 = input("Ingrese una lista de números separados por espacios: ").split()
numeros5 = [float(x) for x in numeros5]
factor = float(input("Ingrese el valor por el cual desea multiplicar los elementos de la lista: "))
numeros5 = [x * factor for x in numeros5]
print(f"La lista con los elementos multiplicados por {factor} es: {numeros5}")

#Ejercicio 6: Eliminar Duplicados Escribe un programa que permita al usuario ingresar una lista de números y elimine los elementos duplicados. Pista:  Utiliza la función set(). 

numeros6 = input("Ingrese una lista de números separados por espacios: ").split()
numeros6 = [float(x) for x in numeros6]
numeros6 = list(set(numeros6))
print(f"La lista sin duplicados es: {numeros6}")

#Ejercicio 7: Promedio de una Lista Escribe un programa que permita al usuario ingresar una lista de números y calcule el promedio de los elementos. 

numeros7 = input("Ingrese una lista de números separados por espacios: ").split()
numeros7 = [float(x) for x in numeros7]
promedio = sum(numeros7) / len(numeros7) if numeros7 else 0
print(f"El promedio de los elementos en la lista es: {promedio}")

#Ejercicio 8: Encontrar Elementos Repetidos Escribe un programa que identifique y muestre los elementos que se repiten en una lista. Pista:  Utiliza un diccionario o un conjunto (set) para hacer el seguimiento de los elementos. 

numeros8 = input("Ingrese una lista de números separados por espacios: ").split()
numeros8 = [float(x) for x in numeros8]
repeated = [x for x in set(numeros8) if numeros8.count(x) > 1]
print(f"Los elementos que se repiten en la lista son: {repeated}")

#Ejercicio 9: Lista de Números Primos Escribe un programa que permita al usuario ingresar una lista de números y filtre los números primos. Pista:  Usa una función para verificar si un número es primo. 

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numeros9 = input("Ingrese una lista de números separados por espacios: ").split()
numeros9 = [float(x) for x in numeros9]
primes = [x for x in numeros9 if es_primo(x)]
print(f"Los números primos en la lista son: {primes}")

#Ejercicio 10: Eliminar un Elemento por su Índice Escribe un programa que permita al usuario ingresar una lista de números y eliminar un elemento en un índice especificado. 
numeros10 = input("Ingrese una lista de números separados por espacios: ").split()
numeros10 = [float(x) for x in numeros10]
index = int(input("Ingrese el índice del elemento que desea eliminar: "))
if 0 <= index < len(numeros10):
    del numeros10[index]
    print(f"La lista después de eliminar el elemento en el índice {index} es: {numeros10}")
else:
    print("Índice fuera de rango.")

#Ejercicio 11: Contar Ocurrencias de un Elemento Escribe un programa que permita al usuario ingresar una lista y un número, y cuente cuántas veces aparece ese número en la lista.

numeros11 = input("Ingrese una lista de números separados por espacios: ").split()
numeros11 = [float(x) for x in numeros11]
element = float(input("Ingrese el número del cual desea contar las ocurrencias: "))
count = numeros11.count(element)
print(f"El número {element} aparece {count} veces en la lista.")

#Ejercicio 12: Sumar Listas Elemento por Elemento Escribe un programa que sume dos listas de números elemento por elemento. Las listas deben tener la misma longitud. 
numeros12 = input("Ingrese la primera lista de números separados por espacios: ").split()
numeros12 = [float(x) for x in numeros12]
numeros13 = input("Ingrese la segunda lista de números separados por espacios: ").split()
numeros13 = [float(x) for x in numeros13]
if len(numeros12) == len(numeros13):
    result = [a + b for a, b in zip(numeros12, numeros13)]
    print(f"La suma de las listas es: {result}")
else:
    print("Las listas deben tener la misma longitud.")

#Ejercicio 13: Explique y ejemplifique la librería NumPy para trabajar con matrices y arrays
# Ejercicio 13: NumPy para matrices y arrays
# Instalar antes: pip install numpy
import numpy as np

print("--- 1. CREACIÓN ---")
# Array 1D y Matriz 2D (array de 2 dimensiones)
arr = np.array([1, 2, 3])
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"Array 1D: {arr} | Forma: {arr.shape}")
print(f"Matriz 2D 3x3:\n{matriz}")

# Creación rápida (muy usada)
ceros = np.zeros((2, 3)) # 2 filas, 3 columnas de ceros
unos = np.ones((2, 2))
identidad = np.eye(3) # Matriz identidad
random = np.random.randint(0, 10, (3, 3)) # Matriz 3x3 con numeros del 0 al 10
print(f"\nRandom 3x3:\n{random}")

print("\n--- 2. INDEXACIÓN Y SLICING ---")
print(f"Elemento [0,1]: {matriz[0, 1]}") # Fila 0, Columna 1
print(f"Columna 1 completa: {matriz[:, 1]}") # : significa "todas las filas"
print(f"Sub-matriz 2x2: \n{matriz[0:2, 1:3]}") # Desde fila 0 a 1, col 1 a 2

# Filtrado booleano
print(f"Mayores a 5: {matriz[matriz > 5]}")

print("\n--- 3. OPERACIONES VECTORIZADAS (sin usar for) ---")
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print(f"a + b = {a + b}")
print(f"a * 2 = {a * 2}")
print(f"Raiz cuadrada de a = {np.sqrt(a)}")

print(f"\nSuma total matriz: {matriz.sum()}")
print(f"Suma por columnas (axis=0): {matriz.sum(axis=0)}")
print(f"Suma por filas (axis=1): {matriz.sum(axis=1)}")
print(f"Promedio: {matriz.mean()}")
print(f"Transpuesta:\n{matriz.T}")

print("\n--- 4. OPERACIONES DE MATRICES REALES ---")
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

producto_elemento_a_elemento = A * B # Multiplica 1*5, 2*6...
producto_matricial = A @ B # Producto matricial real (fila x columna)
print(f"A * B (elemento a elemento):\n{producto_elemento_a_elemento}")
print(f"A @ B (producto matricial):\n{producto_matricial}")
print(f"Determinante de A: {np.linalg.det(A)}")
print(f"Inversa de A:\n{np.linalg.inv(A)}")

print("\n--- 5. EJEMPLO PRACTICO INTEGRADOR ---")
# Filas=alumnos, Columnas=notas de 3 parciales
notas = np.array([[8, 7, 9], [4, 6, 5], [10, 9, 10]])
promedios = notas.mean(axis=1) # Promedio por alumno
print(f"Notas:\n{notas}")
print(f"Promedios por alumno: {promedios}")
print(f"Alumnos aprobados (prom >=6):\n{notas[promedios >= 6]}")