# Ejercicio 12: Analizador y Filtrado de Calificaciones
# Cadena con las notas
notas_cadena = "45, 88, -5, 92, 30, 110, 75, 60, 15"

print("ANALIZADOR DE CALIFICACIONES")
print("=============================")

# 1. Convertir a lista con split
print("\nCadena original: " + notas_cadena)
notas_lista = notas_cadena.split(", ")
print("Lista: " + str(notas_lista))

# Listas para aprobados y reprobados
aprobados = []
reprobados = []
validas = []

print("\nProcesando...")
print("================")

# 2 y 3. Recorrer y validar
for i in range(len(notas_lista)):
    nota_texto = notas_lista[i]
    nota = int(nota_texto)
    
    # Si es invalida, omitir con continue
    if nota < 0 or nota > 100:
        print("Nota " + str(nota) + " es invalida (omitida)")
        continue
    
    # 4. Clasificar
    validas.append(nota)
    if nota >= 60:
        aprobados.append(nota)
        print("Nota " + str(nota) + " APROBADA")
    else:
        reprobados.append(nota)
        print("Nota " + str(nota) + " REPROBADA")

# 5. Mostrar resultados
print("\n================")
print("RESULTADOS")
print("================")

print("\nNotas APROBADAS (>= 60):")
print(aprobados)
print("Total: " + str(len(aprobados)))

print("\nNotas REPROBADAS (< 60):")
print(reprobados)
print("Total: " + str(len(reprobados)))

# Promedio
if len(validas) > 0:
    suma = 0
    for nota in validas:
        suma = suma + nota
    promedio = suma / len(validas)
    print("\nPromedio de notas validas: " + str(promedio))
else:
    print("\nNo hay notas validas")

# Ultimos 2 aprobados con slicing
ultimos_dos = aprobados[-2:]
print("\nUltimos 2 aprobados: " + str(ultimos_dos))

# Resumen
print("\n================")
print("RESUMEN")
print("================")
print("Total de notas procesadas: " + str(len(notas_lista)))
print("Total de notas validas: " + str(len(validas)))
print("Total de notas invalidas: " + str(len(notas_lista) - len(validas)))

if len(validas) > 0:
    tasa = (len(aprobados) * 100) / len(validas)
    print("Tasa de aprobacion: " + str(tasa) + "%")
    print("Nota maxima: " + str(max(validas)))
    print("Nota minima: " + str(min(validas)))

