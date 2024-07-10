Numbers = [1,2,3,4,5,6,7,8,9,0,11,12,13,14,15,16,17,18,19,20]
for i in Numbers:
    print('aqui i es igual a: ', i +1)

for i in range(1, 100):
    print(i)

fruits = ['Manzana', 'Pera', 'Uva', 'Naranja', 'Tomate', 'Banano', 'Sandia']
for fruit in fruits:
    print(fruit)
    if fruit == 'Uva':
        print('Uva encontrado')

x = 0
while x < 5:
    if x == 18:
        break
    print(x)
    x = 20

Numbers = [1,2,3,4,5,6,7,8,9,0,11,12,13,14,15,16,17,18,19,20]
for i in Numbers:
    if i == 3:
        continue
    print('aqui i es igual a: ', i)


Numbers = [1,2,3,4,5,6,7,8,9,0,11,12,13,14,15,16,17,18,19,20]
for i in Numbers:
    if i == 6:
        break
    print('aqui i es igual a: ', i)
