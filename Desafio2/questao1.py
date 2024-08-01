numeros = []

print("Digite dois números de sua escolha abaixo:")
for i in range(2):
    num = float(input(f"Número {i+1}: "))
    numeros.append(num)

if numeros[0] > numeros[1]:
    print(f"O maior número é: {numeros[0]}")
elif numeros[0] < numeros[1]:
    print(f"O maior número é: {numeros[1]}")
else:
    print("Os 2 números são iguais")