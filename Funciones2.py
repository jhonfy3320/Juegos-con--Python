'''#Creando funciones principaes 
def suma(a,b):
    return a + b 

def resta(a,b):
    return a - b 

def multiplicacion(a,b):
    return a * b 

def divisison(a,b):
    return a / b 

def calculator():
    while True:
        print('Selecione uan operacion')
        print('1. suma')
        print('2. resta')
        print('3. multiplicacion')
        print('4. division')
        print('5. salir')

        option = (input('Ingresa tu opción (1,2,3,4,5): '))

        if option == '5':
            print('Saliendo de la calculadora')
            break
        

        if option in ['1','2','3','4']:
            num1 = float(input('Ingrese el primer Numero'))
            num2 = float(input('Ingrese el segundo Numero'))
    
            if option == '1':
                print('La sume es', suma(num1, num2))
            elif option == '2':
                print('La resta es', resta(num1, num2))
            elif option == '3':
                print('La multiplicación es', multiplicacion(num1, num2))
            elif option == '4':
                print('La división es ', divisison(num1, num2))
        else:
            print('porfavor intentar de nuevo')'''


#Ejercicio de Calculadora

def add(a,b):
    return a + b

def substract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b


def calculator():
    while True:
        print("Seleccione una operación")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        option = input("Ingresa su opción (1,2,3,4,5):")

        if option == "5":
            print("Saliendo de la calculadora")
            break
        
        if option in ["1","2","3","4"]:
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))

            if option == "1":
                print("La suma es:", add(num1,num2))
            elif option == "2":
                print("La resta es:", substract(num1,num2))
            elif option == "3":
                print("La multiplicación es:", multiply(num1,num2))
            elif option == "4":
                print("La división es:", divide(num1,num2))   
        else:
            print("Opción no válida, por favor intenta de nuevo.")


calculator()