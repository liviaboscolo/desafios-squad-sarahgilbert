# Nicola - questão 5 desafio 4  
# 5. Crie uma função chamada contar_vogais que recebe uma string
# como parâmetro. Implemente a lógica para contar o número de vogais
# na string e retorne o total de vogais. Solicite ao usuário para inserir uma
# frase e utilize a função para contar as vogais.

def contar_vogais(frase):
    vogais = "aeiouAEIOU"
    contador = 0

    for char in frase:
        if char in vogais:
            contador += 1

    return contador

def main():
    frase = input("Digite uma frase: ")
    total_vogais = contar_vogais(frase)
    print(f"O total de vogais na frase é: {total_vogais}")

if __name__ == "__main__":
    main()