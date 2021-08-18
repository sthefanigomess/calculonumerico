#! /usr/local/bin/python3

import sys

# A função no qual se deseja descobrir a raiz real
def f(x):
    return x**3 - 3

# Requisitamos os valores do usuário
x0 = float(input("Digite a primeira aproximação inicial: "))
x1 = float(input("Digite a segunda aproximação inicial: "))
e1 = float(input("Digite a precisão ε1: "))
e2 = float(input("Digite a precisão ε2: "))

# Verificamos se o modulo de f(x) é menor que a precisao 1
if abs(f(x0)) < e1:
    print(f"A raiz é: {x0}")
    sys.exit()
# Verificamos se o modulo de f(x1) é menor que a precisao 1 ou o modulo de x1 - x0 é menor que a precisao 2
if abs(f(x1)) < e1 or abs(x1 - x0) < e2:
    print(f"A raiz é: {x1}")
    sys.exit()
# No primeiro caso mostramos x0 como a raiz, no segundo caso x1. E em ambos paramos o programa imediatamente
# Declaramos o numero de interações inicialmente como 1
k = 1
# enquanto o numero de interacoes for menor do que 100 continuamos
while k < 100:
    x2 = x1 - (f(x1) / (f(x1) - f(x0))) * (x1 - x0)
    # Caso o modulo de f(x2) seja menor do que o primeiro valor de precisao ou o modulo de x2-x1 seja menor que a segunda precisao
    if abs(f(x2)) < e1 or abs(x2 - x1) < e2:
        # Mostraremos x1 como o valor da raiz, o numero interacoes e pararemos o programa
        print(f"A raiz é: {x1}")
        print(f"O número de interações é: {k}")
        sys.exit()
    # Caso contrario fazemos x0 igual a x1, x1 igual a x2 e incrementamos o numero de interacoes
    x0 = x1
    x1 = x2
    k += 1
# Se o numero de interacoes exeder o limite, apenas dizemos que a raiz nao pode ser encontrada
print("A raiz não foi encontrada.") 
