"""
Rosana - questao 7, desafio 2
Desenvolver um programa que solicite a idade do usuário e identifique se
ele é uma criança, um adolescente, adulto ou idoso.
"""
# Solicitar a idade do usuário
idade = int(input("Olá, informe sua idade: "))

# Identificar a categoria etária
if idade <= 12:
    categoria = "criança"
elif idade <= 17:
    categoria = "adolescente"
elif idade <= 64:
    categoria = "adulto"
else:
    categoria = "idoso"

# Exibir a categoria etária
print(f"Você é um(a) {categoria}.")
