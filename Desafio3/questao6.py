"""
Raquel - questao 6, desafio 3
Faça um programa que permita ao usuário digitar o seu nome e
em seguida mostre o nome do usuário de trás para frente
utilizando somente letras maiúsculas. Dica: lembre−se que ao
informar o nome o usuário pode digitar letras maiúsculas ou
minúsculas.
"""
def name_invert():
    name_input = input("Digite seu nome: ")
    name_update = name_input[::-1].upper()
    print(name_update)
name_invert()