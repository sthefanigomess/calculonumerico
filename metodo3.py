#! /usr/local/bin/python3

import sys

# A função no qual se deseja descobrir a raiz real
def f(x):
    return x**2 + x - 6

# Equação equivalente 
def phi(x):
    return (6 - x)**0.5

# Requisitamos os valores do usuário
x0 = float(input("Digite a aproximação inicial: "))
e1 = float(input("Digite a precisão ε1: "))
e2 = float(input("Digite a precisão ε2: "))

if abs(f(x0)) < e1:
    # Caso o modulo de f(x0), onde x0 é a aproximacao inicial, entao dizemos que a raiz é x0 e paramos o programa
    print(f"A raiz é: {x0}")
    sys.exit()

# Declaramos o numero de interações inicialmente como 1
k = 1
# enquanto o numero de interacoes for menor do que 100 continuamos
while k < 100:
    # Declaramos o valor de x1 como phi(x0)
    x1 = phi(x0)
    # Caso o modulo de f(x1) seja menor do que o primeiro valor de precisao
    # ou x1 -x0 seja menor que o segundo valor de precisao:
    if abs(f(x1)) < e1 or abs(x1-x0) < e2:
        # Mostraremos x1 como o valor da raiz, o numero interacoes e pararemos o programa
        print(f"A raiz é: {x1}")
        print(f"O número de interações é: {k}")
        sys.exit()
    # Caso contrario fazemos x0 = 1, e incrementamos o numero de interacoes
    x0 = x1
    k += 1
# Se o numero de interacoes exeder o limite, apenas dizemos que a raiz nao pode ser encontrada
print("A raiz não foi encontrada.") 
