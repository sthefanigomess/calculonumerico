#! /usr/local/bin/python3

import sys

# Funcao a qual se deseja calcular a raiz
def f(x):
    return x**3 - 3

# A derivada desta mesma funcao
def f1(x):
    return 3*x**2

# Requisitamos os valores do usuário
x0 = float(input("Digite a aproximação inicial: "))
e1 = float(input("Digite a precisão ε1: "))
e2 = float(input("Digite a precisão ε2: "))

if abs(f(x0)) < e1:
    # Caso o modulo de f(x0), onde x0 é a aproximacao inicial, entao dizemos que a raiz é x0 e paramos o programa
    print(f"A raíz é: {x0}")
    sys.exit()
# Declaramos o numero de interações inicialmente como 1
k = 1
# enquanto o numero de interacoes for menor do que 100 continuamos
while k < 100:
    # Declaramos x1 como x0 menos f(x0) sobre a derivada de f em x0
    x1 = x0 - f(x0)/f1(x0)
    # Caso o modulo de f(x1) seja menor do que o primeiro valor de precisao ou o modulo de x1-x0 seja menor que a segunda precisao
    if abs(f(x1)) < e1 or abs(x1 - x0) < e2:
        # Mostraremos x1 como o valor da raiz, o numero interacoes e pararemos o programa
        print(f"A raíz é: {x0}")
        print(f"O número de interações é: {k}")
        sys.exit()
    # Caso contrario fazemos x0 = 1, e incrementamos o numero de interacoes
    x0 = x1
    k += 1
# Se o numero de interacoes exeder o limite, apenas dizemos que a raiz nao pode ser encontrada
print("A raiz não foi encontrada.") 
