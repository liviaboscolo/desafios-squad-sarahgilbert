"""
Letícia - questao 1, desafio 4
Faça um programa, com uma função que necessite de três
argumentos, e que forneça a soma desses três argumentos.
"""
def soma(n1, n2, n3):
    return n1 + n2 + n3

print("Digite abaixo 3 números da sua preferência:")
n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
n3 = float(input("Número 3: "))
print(f"\nA soma destes 3 números é {soma(n1, n2, n3)}")