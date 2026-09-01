# Ejercicio 13: Gestor de Tareas
# Lista para guardar las tareas
tareas = []

print("BIENVENIDO AL GESTOR DE TAREAS")
print("===============================")

# Menu principal con while
seguir = True
while seguir:
    print("\nOpciones:")
    print("1 - Agregar tarea")
    print("2 - Eliminar tarea")
    print("3 - Ver tareas")
    print("4 - Salir")
    
    opcion = input("\nElige una opcion: ")
    
    # Opcion 1: Agregar
    if opcion == "1":
        tarea_nueva = input("Escribe el nombre de la tarea: ")
        
        # Verificar si ya existe con 'in'
        if tarea_nueva in tareas:
            print("ERROR: Esa tarea ya existe!")
        else:
            tareas.append(tarea_nueva)
            print("Tarea agregada!")
    
    # Opcion 2: Eliminar
    elif opcion == "2":
        tarea_borrar = input("Que tarea quieres borrar?: ")
        
        # Verificar con 'in' si existe
        if tarea_borrar in tareas:
            tareas.remove(tarea_borrar)
            print("Tarea eliminada!")
        else:
            print("ERROR: Esa tarea no existe!")
    
    # Opcion 3: Ver resumen
    elif opcion == "3":
        print("\n--- RESUMEN ---")
        print("Total de tareas:", len(tareas))
        
        if len(tareas) == 0:
            print("No hay tareas")
        else:
            # Primeras 3 con slicing
            primeras = tareas[:3]
            print("\nPrimeras 3 tareas:")
            for i in range(len(primeras)):
                print(str(i + 1) + ". " + primeras[i])
        
        # Si hay mas de 3, mostrar todas
        if len(tareas) > 3:
            print("\nTodas las tareas:")
            for i in range(len(tareas)):
                print(str(i + 1) + ". " + tareas[i])
    
    # Opcion 4: Salir
    elif opcion == "4":
        print("\nHasta luego!")
        print("Tareas pendientes:", len(tareas))
        if len(tareas) > 0:
            print("Lista:")
            for i in range(len(tareas)):
                print("- " + tareas[i])
        break  # Salir del while
    
    else:
        print("Opcion invalida!")

