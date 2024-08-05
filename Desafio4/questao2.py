"""
Lívia - questao 2, desafio 4
 Reverso do número. Faça uma função que retorne o reverso de um
número inteiro informado. Por exemplo: 127 -> 721.
"""
def invertido_n(n):
  
    n_invertido = int(str(n)[::-1])
    return n_invertido

n = int(input("Digite um número: "))

n_invertido = invertido_n(n)
print(f"O reverso do {n} é {n_invertido}")

