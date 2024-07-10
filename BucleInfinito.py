def mostrar_menu():
    print("\nMenú:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")

while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        print("Has elegido la Opción 1")
    elif opcion == "2":
        print("Has elegido la Opción 2")
    elif opcion == "3":
        print("Has elegido la Opción 3")
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")
