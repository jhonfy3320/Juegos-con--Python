try:
    resultado = 10 / 0
except ZeroDivisionError:
    pass  # Simplemente ignora la excepción
else:
    print("La división se realizó con éxito.")
finally:
    print("Esto se ejecuta siempre.")


def dividir():
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = a / b
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    except ValueError:
        print("Error: Entrada no válida. Por favor ingrese números.")
    else:
        print(f"El resultado de la división es: {resultado}")
    finally:
        print("Operación completada.")

# Llamar a la función
dividir()
