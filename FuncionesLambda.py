add = lambda a, b: a + b
print(add(20, 8))

multiply= lambda a, b: a * b
print(multiply(20, 8))

sustrac = lambda a, b: a - b
print(sustrac(20, 8)) 

división = lambda a, b: a / b
print(división(20, 8))

#Cudrado de cada numero 
numbers = range(101)
squared_numbers = list(map(lambda x: x**2, numbers))
print('Cuadrados: ', squared_numbers)

print('#'*100)
#pares de cada numero 
even_numbers = list(filter(lambda x: x%2 == 0, numbers))
print('pares: ', even_numbers)

print('#'*100)
#pares de cada numero 
impar_numbers = list(filter(lambda x: x%2  != 0, numbers))
print('impares: ', impar_numbers)