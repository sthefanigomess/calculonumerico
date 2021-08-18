#! /usr/local/bin/python3

# A função no qual se deseja descobrir a raiz real
def f(x):
    return x**3 - 3

print("Declare o intervalo.")
# Requisitamos os valores do usuário
a = float(input("valor de a: "))
b = float(input("valor de b: "))
e = float(input("valor de ε: "))

# Verifica se o 0 está no intervalo
if (f(a) * f(b) < 0):
    # Declaramos o numero de interações inicialmente como 1
    k = 1
    # Declaramos a variavel x1
    x1 = 0
    # Enquanto o modulo de a-b for maior do que a precisao, fazemos:
    while abs(b-a) > e:
        # Declaramos um x1 como a média entre a e b
        x1 = (a+b)/2
        # Se f(x1) for 0, entao paramos o loop
        if f(x1) == 0:
            break
        # Verificamos se a raiz está entre a e x1:
        if f(a) * f(x1) < 0:
            # Caso esteja, definimos o novo intervalo como de a até x1 
            b = x1
        else:
            # Caso contratio, definimos o novo intervalo de x1 até b
            a = x1
        # Por fim incrementamos o numero de interacoes
        k += 1 
    # Uma vez que o loop pare, mostramos na tela o valor de x1, o intervalo e o número de interacoes
    print(f"O valor da raiz é: {x1}.")
    print(f"O intervalo é :[{a}, {b}].")
    print(f"O numero de interações é: {k}.")
# Caso f(a) * f(b) seja maior que zero, 
# mostramos apenas que o valor nao pertence ao intervalo original
else:
    print("Não há raiz real neste intervalo.")

