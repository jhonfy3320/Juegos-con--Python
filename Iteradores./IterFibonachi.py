# Iterador que produce números de Fibonacci
class FibonacciIterador:
    def __init__(self, maximo):
        self.maximo = maximo
        self.a = 0
        self.b = 1
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.contador >= self.maximo:
            raise StopIteration
        self.contador += 1
        resultado = self.a
        self.a, self.b = self.b, self.a + self.b
        return resultado

# Generador que produce números de Fibonacci
def fibonacci_generador(maximo):
    a, b = 0, 1
    for _ in range(maximo):
        yield a
        a, b = b, a + b

# Uso del iterador
fib_iter = FibonacciIterador(10)
print("Fibonacci con Iterador:")
for num in fib_iter:
    print(num)

# Uso del generador
fib_gen = fibonacci_generador(10)
print("\nFibonacci con Generador:")
for num in fib_gen:
    print(num)


print('#'*100)
# Generador infinito
def generador_infinito():
    num = 0
    while True:
        yield num
        num += 1

# Crear un generador infinito
gen_inf = generador_infinito()

# Obtener los primeros 10 números del generador infinito
for _ in range(10):
    print(next(gen_inf))

print('#'*100)
# Generador de números primos
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generador_primos():
    num = 2
    while True:
        if es_primo(num):
            yield num
        num += 1

# Crear un generador de números primos
gen_primos = generador_primos()

# Obtener los primeros 10 números primos
for _ in range(10):
    print(next(gen_primos))
