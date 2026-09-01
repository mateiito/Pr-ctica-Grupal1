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