"""
Letícia - questao 1, desafio 3
1. Utilizando listas faça um programa que faça 5 perguntas para uma
pessoa sobre um crime.
As perguntas são:
""Telefonou para a vítima?""
""Esteve no local do crime?""
""Mora perto da vítima?""
""Devia para a vítima?""
""Já trabalhou com a vítima?""
O programa deve no final emitir uma classificação sobre a participação
da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser
classificada como ""Suspeita"", entre 3 e 4 como ""Cúmplice"" e 5 como
""Assassino"".
Caso contrário,ele será classificado como""Inocente"".
"""
perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]
respostas = []
cont = 0

print("Bem-vindo(a) ao interrogatório do crime. Responda as perguntas abaixo com sim ou não [s/n]\n")
for p in perguntas:
    r = input(f"{p} ")
    respostas.append(r)
    if r.lower() == 's':
        cont += 1

print("cont no final: " ,cont, "\n")
if cont == 2:
    print("Com base nas suas respostas, você foi é considerado SUSPEITO do crime")
elif cont == 3 or cont == 4:
    print("Com base nas suas respostas, você foi é considerado CÚMPLICE do crime")
elif cont == 5:
    print("Com base nas suas respostas, você é o ASSASSINO")
else:
    print("Com base nas suas respostas, você é INOCENTE")