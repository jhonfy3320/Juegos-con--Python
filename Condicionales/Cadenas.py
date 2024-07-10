name = '''FREDDY
sebas
NICO
kevin
EMANUEL
ALEJANDRO
'''
caracter = 'c'
print(name)
print(caracter)
print(type(caracter))

# Indexacion de caracteres 
name2 = 'freddy tavera '
print(name2[2])

# concatenacion o suma y multiplicacion de caracteres 
moder = 'Luz elena '
print(name + name2 + '' + moder)
print(name * 5)

# Longitudes de las variables 
print(len(name))
print(len(name2))
print(len(moder))

#metodos 
print(name.lower())
print(name.upper())
print(name.strip())

#Capitaliza la primera letra.

texto = "hola mundo"
print(texto.capitalize())  # "Hola mundo"

#title()
#Capitaliza la primera letra de cada palabra.
texto = "hola mundo"
print(texto.title())  # "Hola Mundo"

#strip()
#Elimina los espacios en blanco al inicio y al final.
texto = "  hola  "
print(texto.strip())  # "hola"

#replace(old, new)
#Reemplaza partes de la cadena.
texto = "hola mundo"
print(texto.replace("mundo", "Python"))  # "hola Python"

#split(sep)
#Divide la cadena en una lista según el separador.
texto = "hola,mundo,Python"
print(texto.split(","))  # ['hola', 'mundo', 'Python']

#join(iterable)
#Une elementos de un iterable en una sola cadena.
lista = ["hola", "mundo"]
print(" ".join(lista))  # "hola mundo"

#find(sub)
#Busca una subcadena y devuelve el índice de su primera aparición.
texto = "hola mundo"
print(texto.find("mundo"))  # 5

#startswith(prefix) y endswith(suffix)
#Verifica si la cadena empieza o termina con una subcadena.
texto = "hola mundo"
print(texto.startswith("hola"))  # True
print(texto.endswith("mundo"))  # True

#Ejemplo Completo:
frase = "  Bienvenido a Python!  "
frase = frase.strip().replace("Python", "el mundo de Python").upper()
print(frase)  # "BIENVENIDO A EL MUNDO DE PYTHON!"