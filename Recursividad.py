# Factorial 
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
factorial_5 = print(factorial(100))

print('#'*100)
# Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

number = 10
print(fibonacci(number))

print('#'*100)
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
        return memo[n]

# Ejemplo de uso
print(fibonacci_memo(20))  # Salida: 55

print('#'*100)
def sumatoria(n):
    if n == 0:
        return 0
    else:
        return n + sumatoria(n - 1)

# Probar la función con varios valores
for i in range(101):
    print(f"Sumatoria de {i} es: {sumatoria(i)}")
