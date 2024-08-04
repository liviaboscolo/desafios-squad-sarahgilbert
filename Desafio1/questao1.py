"""
Letícia - questao 1, desafio 1
Faça um Programa que peça dois números, realize as principais
operações soma, subtração, multiplicação, divisão
"""
def soma(num1, num2):
    print(f"Soma: {num1 + num2}")

def subt(num1, num2):
    print(f"Subtração: {num1 - num2}")

def mult(num1, num2):
    print(f"Multiplicação: {num1 * num2}")

def div(num1, num2):
    try:
        print(f"Divisão: {num1 / num2}")
    except ZeroDivisionError:
        print("Não permitida a divisão por zero")

print("Digite dois números de sua escolha abaixo:")
num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))

print("Resultado das operações básicas:")
soma(num1, num2)
subt(num1, num2)
mult(num1, num2)
div(num1, num2)