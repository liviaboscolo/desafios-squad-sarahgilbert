# Ler três números inteiros do usuário
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

# Criar uma lista com os números
numeros = [num1, num2, num3]

# Ordenar a lista em ordem crescente
numeros.sort()

# Exibir os números em ordem crescente
print("Os números em ordem crescente são:", numeros)
