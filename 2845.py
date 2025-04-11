# Escreva a sua solução aqui
# Code your solution here
# Escriba su solución aquí
import math

def e_coprimo(a, b):
    return math.gcd(a, b) == 1

def totiente(n):
    result = n
    i = 2
    while i * i <= n:
        if n % i == 0:
            while n % i == 0:
                n //= i
            result -= result // i
        i += 1
    if n > 1:
        result -= result // n
    return result

def descobrir_duende(N, lista):
    lista_set = set(lista)
    max_val = max(lista) + 1
    for x in range(max_val, 100000):  # Limite razoável
        coprimos = [i for i in range(1, x) if math.gcd(i, x) == 1]
        if len(coprimos) == N and set(coprimos) == lista_set:
            return x
    return -1  # Se não encontrar

# Exemplo de uso:
N = int(input())
lista = list(map(int, input().split()))
print(descobrir_duende(N, lista))

.