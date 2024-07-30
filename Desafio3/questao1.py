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