#! /usr/local/bin/python3

# Usando as bibliotecas math e sys
from math import exp
import sys

# A função no qual se deseja descobrir a raiz real
def f(x):
    return x*exp(x) - 1

# Requisitamos os valores do usuário
a  = float(input('Digite o valor do inicio do intervalo "a": '))
b  = float(input('Digite o valor do fim do intervalo "b": '))
e1 = float(input('Digite o valor de ε1: '))
e2 = float(input('Digite o valor do ε2: '))

# Verifica se o 0 está no intervalo
if f(a)*f(b) > 0:
    print('O raiz nao está no intervalo pois f(a)*f(b) > 0')
    # Caso nao esteja saimos imediatamente do programa
    sys.exit()


# Verificamos se o modulo de f(a) é menor do que a segunda precisao
if abs(f(a)) < e2:
    print(f'O valor aproximado para a raiz é: {a}')
    sys.exit()
# Verificamos se o modulo de f(b) é menor do que a segunda precisao
elif abs(f(b)) < e2:
    print(f'O valor aproximado para a raiz é: {b}')
    sys.exit()
# Em ambos os casos mostramos o valor de a ou b e saimos do programa
else:
    # Declaramos o numero de interações inicialmente como 1
    k = 1
    # Declaramos o valor de M como f(a)
    m = f(a)
    # Enquanto o modulo de a-b for maior do que a precisao, fazemos:
    while b-a > e1:
        # declaramos um valor de x como:
        x = (a*f(b) - b*f(a)) / (f(b) - f(a))
        if abs(f(x)) < e2:
            # Caso o modulo de f(x) for maenor do que a precisao 2 mostramos o valor de x como a raiz e saimos do programa
            print(f'Com {k} interaçoes, o valor aproximado da raiz é: {x}')
            sys.exit()
        elif m*f(x) > 0:
            # Caso M*f(x) seja maior do que zero 'a' será igual a 'x'
            a = x
        else:
            # Caso contratio 'b' será igual a 'x'
            b = x
        # Por fim incrementamos o numero de interacoes
        k += 1
    # Uma vez que o loop pare Retornamos como a raiz a media entre a e b
    print(f'Com {k} interaçoes, o valor aproximado da raiz é {a+b/2}')
