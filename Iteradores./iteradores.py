# Ejemplo de iterador 

# Iterando una cadena de texto 
text = 'Hola a todos estamos aprendiendo python. Los estraño NEKASMFYPY'
iter_text = iter(text)
print(text)
print(iter_text)

for char in iter_text:
    print(char)

# crear una lista 
my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(my_list)
my_iter = iter(my_list)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

# Creando un iterador para selecionar numeros impares 

# Numeros pares 
limite = 100
odd_itter =iter(range(0,limite+1,2))
for num in odd_itter:
    print(num)


#Numeros impares 
limite = 100
odd_itter =iter(range(1,limite+1,2))
for num in odd_itter:
    print(num)

#Generador, secuencia de numeros sobre los cuales podemos iterar 
def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6
    yield 7
    yield 8
    yield 9
    yield 10
for value in my_generator():
    print(value)


print('#'* 100)
#Fibonachi
def fibonachi(limit):
    a, b = 0,1
    while a< limit:
        yield a
        a, b = b, a+b
for num in fibonachi(100):
    print(num)